document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('input[type="file"]').addEventListener('change', function() {
        var numFiles = this.files.length;

        var label = document.querySelector('.custom-file-label');
        label.textContent = numFiles + (numFiles === 1 ? ' arquivo selecionado' : ' arquivos selecionados');
        // rest of the code
    });
    
});
