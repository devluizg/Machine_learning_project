import { useEffect, useState } from 'react';

// Cole aqui a URL do Web App gerada no Google Apps Script da sua planilha
// (ou defina VITE_GOOGLE_SCRIPT_URL no arquivo .env antes do build).
export const GOOGLE_SCRIPT_URL: string =
  import.meta.env.VITE_GOOGLE_SCRIPT_URL ??
  'https://script.google.com/macros/s/AKfycbz41lkTQqjEYGwkxlYTja9K8yVmQnEpTeiu6JM2F2qDy2H_r0evCHyE-pcTnrHPgP8y/exec';

export interface TableQuestionSpec {
  columns: readonly string[];
  rows: readonly {
    id: string;
    label: string;
    placeholder?: string;
  }[];
}

export interface ActivityQuestion {
  id: string;
  title: string;
  prompt: string;
  rows?: number;
  table?: TableQuestionSpec;
}

export interface LessonActivitySpec {
  moduleId: string;
  lessonTitle: string;
  situation: string;
  questions: readonly ActivityQuestion[];
}

interface StoredLessonState {
  answers: Record<string, string>;
  updatedAt?: string;
  submittedAt?: string;
}

const STUDENT_NAME_KEY = 'ml-project-student-name';

function loadStudentName(): string {
  try {
    return window.localStorage.getItem(STUDENT_NAME_KEY) ?? '';
  } catch {
    return '';
  }
}

function loadLessonState(moduleId: string): StoredLessonState {
  try {
    const raw = window.localStorage.getItem(`ml-project-respostas-${moduleId}`);
    if (!raw) return { answers: {} };
    const parsed = JSON.parse(raw) as StoredLessonState;
    return {
      answers: parsed.answers ?? {},
      updatedAt: parsed.updatedAt,
      submittedAt: parsed.submittedAt,
    };
  } catch {
    return { answers: {} };
  }
}

function loadPredictionNote(moduleId: string): string {
  try {
    return window.localStorage.getItem(`ml-project-prediction-${moduleId}`) ?? '';
  } catch {
    return '';
  }
}

function cellKey(questionId: string, rowId: string, colIndex: number): string {
  return `${questionId}__${rowId}__c${colIndex}`;
}

function formatQuestionAnswer(q: ActivityQuestion, answers: Record<string, string>): string {
  if (!q.table) {
    return (answers[q.id] ?? '').trim();
  }
  const valueCols = q.table.columns.slice(1);
  const formattedRows = q.table.rows.map((row) => {
    const colsText = valueCols
      .map((colName, idx) => {
        const val = (answers[cellKey(q.id, row.id, idx)] ?? '').trim() || '(em branco)';
        return valueCols.length === 1 ? val : `${colName}: ${val}`;
      })
      .join(' | ');
    return `${row.label}: ${colsText}`;
  });
  return formattedRows.join('\n');
}

function isQuestionAnswered(q: ActivityQuestion, answers: Record<string, string>): boolean {
  if (!q.table) {
    return (answers[q.id] ?? '').trim().length > 0;
  }
  const valueColCount = q.table.columns.length - 1;
  return q.table.rows.some((row) =>
    Array.from({ length: valueColCount }, (_, idx) => (answers[cellKey(q.id, row.id, idx)] ?? '').trim().length > 0).some(Boolean),
  );
}

function triggerDownload(filename: string, content: string, mimeType: string) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

export function LessonActivitySheet({ spec }: { spec: LessonActivitySpec }) {
  const [studentName, setStudentName] = useState<string>(() => loadStudentName());
  const [answers, setAnswers] = useState<Record<string, string>>(() => loadLessonState(spec.moduleId).answers);
  const [savedTime, setSavedTime] = useState<string | undefined>(() => loadLessonState(spec.moduleId).updatedAt);
  const [submittedAt, setSubmittedAt] = useState<string | undefined>(() => loadLessonState(spec.moduleId).submittedAt);
  const [sending, setSending] = useState(false);
  const [sendError, setSendError] = useState<string | null>(null);
  const [confirmClear, setConfirmClear] = useState(false);

  useEffect(() => {
    const loaded = loadLessonState(spec.moduleId);
    setAnswers(loaded.answers);
    setSavedTime(loaded.updatedAt);
    setSubmittedAt(loaded.submittedAt);
    setSendError(null);
    setConfirmClear(false);
  }, [spec.moduleId]);

  const persistLesson = (nextAnswers: Record<string, string>, nextUpdatedAt?: string, nextSubmittedAt?: string) => {
    try {
      window.localStorage.setItem(
        `ml-project-respostas-${spec.moduleId}`,
        JSON.stringify({ answers: nextAnswers, updatedAt: nextUpdatedAt, submittedAt: nextSubmittedAt }),
      );
    } catch {
      // Ignora erro de armazenamento local bloqueado
    }
  };

  const handleNameChange = (value: string) => {
    setStudentName(value);
    setSendError(null);
    try {
      window.localStorage.setItem(STUDENT_NAME_KEY, value);
    } catch {
      // Ignora erro de armazenamento local bloqueado
    }
  };

  const handleAnswerChange = (key: string, value: string) => {
    if (submittedAt) return;
    const nextAnswers = { ...answers, [key]: value };
    const now = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
    setAnswers(nextAnswers);
    setSavedTime(now);
    persistLesson(nextAnswers, now, submittedAt);
  };

  const handleSubmitToTeacher = async () => {
    const trimmedName = studentName.trim();
    if (!trimmedName) {
      setSendError('Digite seu nome completo antes de enviar.');
      return;
    }
    if (!GOOGLE_SCRIPT_URL) {
      setSendError('O envio online ainda não foi configurado. Use "Baixar respostas (.txt)" por enquanto.');
      return;
    }

    setSending(true);
    setSendError(null);

    const payload = {
      studentName: trimmedName,
      moduleId: spec.moduleId,
      lessonTitle: spec.lessonTitle,
      submittedIso: new Date().toISOString(),
      initialPrediction: loadPredictionNote(spec.moduleId).trim(),
      responses: spec.questions.map((q) => ({
        id: q.id,
        title: q.title,
        answer: formatQuestionAnswer(q, answers),
      })),
    };

    try {
      await fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload),
      });
      const now = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
      setSubmittedAt(now);
      persistLesson(answers, savedTime ?? now, now);
    } catch {
      setSendError('Não foi possível enviar pela internet. Clique em "Baixar respostas (.txt)" para não perder seu registro.');
    } finally {
      setSending(false);
    }
  };

  const handleDownloadTxt = () => {
    const nameLabel = studentName.trim() || 'sem-nome';
    const dateStr = new Date().toLocaleDateString('pt-BR');
    const prediction = loadPredictionNote(spec.moduleId);
    const lines: string[] = [
      `============================================================`,
      `FOLHA DIGITAL DO ESTUDANTE — ${spec.lessonTitle}`,
      `============================================================`,
      `Estudante: ${nameLabel}`,
      `Data: ${dateStr}`,
      ``,
      `Situação-problema:`,
      spec.situation,
      ``,
    ];

    if (prediction.trim()) {
      lines.push(`--- Previsão inicial (antes de alterar o controle) ---`);
      lines.push(prediction.trim());
      lines.push(``);
    }

    spec.questions.forEach((q) => {
      lines.push(`--- ${q.title} ---`);
      lines.push(`Pergunta: ${q.prompt}`);
      lines.push(`Resposta:\n${formatQuestionAnswer(q, answers) || '(em branco)'}`);
      lines.push(``);
    });

    const safeName = nameLabel.toLowerCase().replace(/[^a-z0-9_-]+/g, '_');
    triggerDownload(
      `respostas_${spec.moduleId}_${safeName}.txt`,
      lines.join('\n'),
      'text/plain;charset=utf-8',
    );
  };

  const handleClear = () => {
    if (!confirmClear) {
      setConfirmClear(true);
      return;
    }
    setAnswers({});
    setSavedTime(undefined);
    setSubmittedAt(undefined);
    setSendError(null);
    setConfirmClear(false);
    try {
      window.localStorage.removeItem(`ml-project-respostas-${spec.moduleId}`);
      window.localStorage.removeItem(`ml-project-prediction-${spec.moduleId}`);
    } catch {
      // Ignora erro de armazenamento local bloqueado
    }
  };

  const answeredCount = spec.questions.filter((q) => isQuestionAnswered(q, answers)).length;
  const isLocked = Boolean(submittedAt);

  return (
    <section className="activity-sheet-card" aria-label={`Atividade da aula: ${spec.lessonTitle}`}>
      <div className="activity-sheet-head">
        <div>
          <span className="section-number">05 / ATIVIDADE DA SEQUÊNCIA DIDÁTICA</span>
          <h3>{spec.lessonTitle}</h3>
        </div>
        <div className="activity-participant-box">
          <label htmlFor={`student-name-${spec.moduleId}`}>Seu nome completo</label>
          <input
            disabled={isLocked}
            id={`student-name-${spec.moduleId}`}
            onChange={(e) => handleNameChange(e.target.value)}
            placeholder="Digite seu nome completo"
            type="text"
            value={studentName}
          />
        </div>
      </div>

      <p className="activity-situation">
        <strong>Situação:</strong> {spec.situation}
      </p>

      <div className="activity-questions-grid">
        {spec.questions.map((q) => (
          <div className="activity-question-item" key={q.id}>
            <div className="activity-question-header">
              <strong>{q.title}</strong>
              <span>{q.prompt}</span>
            </div>
            {q.table ? (
              <div className="table-scroll">
                <table className="activity-fill-table">
                  <thead>
                    <tr>
                      {q.table.columns.map((col) => (
                        <th key={col}>{col}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {q.table.rows.map((row) => (
                      <tr key={row.id}>
                        <td className="activity-table-label">{row.label}</td>
                        {q.table!.columns.slice(1).map((colName, colIdx) => {
                          const key = cellKey(q.id, row.id, colIdx);
                          return (
                            <td key={key}>
                              <input
                                aria-label={`${row.label} — ${colName}`}
                                disabled={isLocked}
                                onChange={(e) => handleAnswerChange(key, e.target.value)}
                                placeholder={row.placeholder ?? 'Digite aqui...'}
                                type="text"
                                value={answers[key] ?? ''}
                              />
                            </td>
                          );
                        })}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <textarea
                aria-label={q.title}
                disabled={isLocked}
                id={`q-${spec.moduleId}-${q.id}`}
                onChange={(e) => handleAnswerChange(q.id, e.target.value)}
                placeholder="Escreva sua resposta e explique como pensou..."
                rows={q.rows ?? 3}
                value={answers[q.id] ?? ''}
              />
            )}
          </div>
        ))}
      </div>

      {sendError && (
        <p className="activity-error" role="alert">
          {sendError}
        </p>
      )}

      {submittedAt && (
        <p className="activity-submitted-banner" role="status">
          Respostas enviadas para o professor às {submittedAt}. Os campos foram bloqueados nesta tela.
        </p>
      )}

      <div className="activity-sheet-footer">
        <div className="activity-status">
          <span>
            {answeredCount}/{spec.questions.length} respondida(s)
            {savedTime ? ` · Salvo neste computador às ${savedTime}` : ' · Salvamento automático local'}
          </span>
          <small>Ao clicar em enviar, uma cópia vai para a planilha do professor (e você também pode baixar em .txt).</small>
        </div>
        <div className="activity-actions">
          <button
            className="primary-button"
            disabled={sending || isLocked}
            onClick={handleSubmitToTeacher}
            type="button"
          >
            {sending ? 'Enviando...' : isLocked ? 'Enviado ao professor' : 'Enviar respostas para o professor'}
          </button>
          <button className="step-button" onClick={handleDownloadTxt} type="button">
            Baixar respostas (.txt)
          </button>
          <button className="reset-button" onClick={handleClear} type="button">
            {confirmClear ? 'Confirmar limpeza' : 'Limpar para outro aluno'}
          </button>
        </div>
      </div>
    </section>
  );
}
