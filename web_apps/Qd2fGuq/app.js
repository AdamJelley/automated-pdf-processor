/*
 * For more information, refer to the "Javascript API" documentation:
 * https://doc.dataiku.com/dss/latest/api/js/index.html
 */

let exportButton = document.getElementById('export-button');

exportButton.addEventListener('click', function (event) {
    let analysisName = document.getElementById('analysis-name');
    let analysisValue = analysisName.value || '(no analysis name typed)';
    let datasetName = document.getElementById('dataset-name');
    let datasetValue = datasetName.value || '(no dataset chosen)';
    let datasetColumn = document.getElementById('dataset-column');
    let columnValue = datasetColumn.value || '(no column chosen)';
    let rowsLimitValue = document.getElementById('rows-limit').checked;
    let exportValue = document.querySelector('input[name="export"]:checked').value || '(no export format typed)';

    alert('Now YOU should code something if you really want an export. For now, your parameters are: ' + analysisValue + ' / ' + datasetValue  + ' / ' + columnValue + ' / ' + rowsLimitValue + ' / ' + exportValue);
    event.preventDefault();
});

/* Fetch dataset sample */
let fetchButton = document.getElementById('fetch-button');
let datasetName = document.getElementById('dataset-name');
let messageContainer = document.getElementById('message');
let selectedDataset = {};

function displayMessage(messageText, messageClassname) {
    messageContainer.innerHTML = messageText;
    messageContainer.className = '';
    if (messageClassname && messageClassname.length > 0) {
        messageContainer.className = messageClassname;
    }
}

function clearMessage() {
    displayMessage('');
}

function displayFailure() {
    displayMessage('The dataset cannot be retrieved. Please check the dataset name or the API Key\'s permissions in the "Settings" tab of the webapp.', 'error-message');
}

function displayDataFrame(dataFrame) {
    let columnsNames = dataFrame.getColumnNames();
    let line = '------------------------------';
    let text = selectedDataset.name + '\n'
        + line + '\n'
        + dataFrame.getNbRows() + ' Rows\n'
        + columnsNames.length + ' Columns\n'
        + '\n' + line + '\n'
        + 'Columns names: \n';
    columnsNames.forEach(function(columnName) {
        text += columnName + ', ';
    });
    displayMessage(text);
}

fetchButton.addEventListener('click', function(event) {
    clearMessage();
    selectedDataset.name = document.getElementById('dataset-to-fetch').value;
    dataiku.fetch(selectedDataset.name, function(dataFrame) {
        selectedDataset.dataFrame = dataFrame;
        displayDataFrame(dataFrame);
    }, function() {
        displayFailure();
    });
    return false;
});
