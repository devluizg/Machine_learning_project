import { describe, expect, it } from 'vitest';
import { modelComparisons, moduleLessonContexts, studentLessons, teacherMeetings } from './coursePlan';

describe('apoio à sequência didática', () => {
  it('compara os cinco modelos sem duplicar identificadores', () => {
    expect(modelComparisons).toHaveLength(5);
    expect(new Set(modelComparisons.map((item) => item.id)).size).toBe(5);
    for (const item of modelComparisons) {
      expect(item.purpose).toBeTruthy();
      expect(item.output).toBeTruthy();
      expect(item.limit).toBeTruthy();
    }
  });

  it('mantém oito encontros de cinquenta minutos', () => {
    expect(teacherMeetings).toHaveLength(8);
    for (const meeting of teacherMeetings) {
      expect(meeting.phases.reduce((total, phase) => total + phase.minutes, 0)).toBe(50);
    }
  });

  it('reserva o encontro final para produção sem recurso do site', () => {
    expect(teacherMeetings[7]?.route).toBeUndefined();
    expect(teacherMeetings[7]?.title).toBe('Síntese individual');
  });

  it('apresenta ao estudante o percurso completo sem expor o instrumento final', () => {
    expect(studentLessons).toHaveLength(8);
    expect(studentLessons[7]?.siteUse).toBe('sem-site');
    expect(studentLessons[7]?.route).toBeUndefined();
  });

  it('liga cada módulo ao encontro correspondente', () => {
    expect(Object.keys(moduleLessonContexts)).toHaveLength(5);
    expect(moduleLessonContexts['regressao-linear'].meeting).toBe(2);
    expect(moduleLessonContexts.kmeans.meeting).toBe(6);
  });

  it('publica somente os roteiros didáticos intermediários', () => {
    expect(teacherMeetings[0]?.material).toBeUndefined();
    expect(teacherMeetings[7]?.material).toBeUndefined();
    expect(teacherMeetings.slice(1, 7).every((meeting) => meeting.material?.endsWith('.pdf'))).toBe(true);
  });
});
