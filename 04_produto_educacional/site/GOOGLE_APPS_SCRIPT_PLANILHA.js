/* eslint-disable */
/**
 * INSTRUÇÕES RÁPIDAS (2 MINUTOS):
 * 1. Crie uma nova planilha no seu Google Drive (ex.: "Respostas_ML_Projeto").
 * 2. No menu da planilha, clique em: Extensões -> Apps Script.
 * 3. Apague o código padrão e cole todo este arquivo.
 * 4. Clique em "Implantar" (canto superior direito) -> "Nova implantação".
 * 5. Em "Selecionar tipo", escolha "App da Web".
 * 6. Em "Executar como": "Eu (seu e-mail)".
 * 7. Em "Quem pode acessar": "Qualquer pessoa".
 * 8. Clique em "Implantar", autorize o acesso à sua planilha e copie a URL do App da Web.
 * 9. Cole essa URL na constante GOOGLE_SCRIPT_URL em:
 *    04_produto_educacional/site/src/learning/LessonActivitySheet.tsx
 */

function doPost(e) {
  try {
    var raw = e.postData && e.postData.contents ? e.postData.contents : '{}';
    var data = JSON.parse(raw);

    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheetName = (data.moduleId || 'respostas').toString().substring(0, 30);
    var sheet = ss.getSheetByName(sheetName);

    var responses = Array.isArray(data.responses) ? data.responses : [];

    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
      var headers = ['Data/Hora', 'Nome do Estudante', 'Previsão Inicial'];
      for (var i = 0; i < responses.length; i++) {
        headers.push(responses[i].title || responses[i].id || ('Questão ' + (i + 1)));
      }
      sheet.appendRow(headers);
      sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    }

    var row = [
      new Date(),
      data.studentName || '',
      data.initialPrediction || ''
    ];
    for (var j = 0; j < responses.length; j++) {
      row.push(responses[j].answer || '');
    }

    sheet.appendRow(row);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
