import { useState } from 'react';

export interface QuickCheckSpec {
  question: string;
  options: readonly string[];
  correct: number;
  explanation: string;
  retryHint: string;
}

export function QuickCheck({ spec }: { spec: QuickCheckSpec }) {
  const [selected, setSelected] = useState<number | null>(null);
  const [checked, setChecked] = useState(false);
  const isCorrect = selected === spec.correct;

  return <section className="quick-check" aria-label="Verifique sua compreensão">
    <span className="tiny-label">VERIFIQUE O QUE ENTENDEU</span>
    <h3>{spec.question}</h3>
    <fieldset>
      <legend className="sr-only">Escolha uma resposta</legend>
      {spec.options.map((option, index) => <label className="quick-option" key={option}>
        <input checked={selected === index} name="quick-check" onChange={() => { setSelected(index); setChecked(false); }} type="radio" />
        <span>{option}</span>
      </label>)}
    </fieldset>
    <button className="primary-button" disabled={selected === null} onClick={() => setChecked(true)} type="button">Conferir resposta</button>
    {checked && <p aria-live="polite" className={`quick-feedback ${isCorrect ? 'is-correct' : 'needs-review'}`}>
      <strong>{isCorrect ? 'Isso mesmo.' : 'Ainda não.'}</strong> {isCorrect ? spec.explanation : spec.retryHint}
    </p>}
  </section>;
}
