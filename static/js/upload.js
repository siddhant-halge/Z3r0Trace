const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileElem");
const browseBtn = document.getElementById("browse-btn");
const fileName = document.getElementById("file-name");

browseBtn.addEventListener("click", () => {
    fileInput.click();
});

fileInput.addEventListener("change", () => {

    if(fileInput.files.length > 0){

        fileName.innerText = fileInput.files[0].name;

    }

});

["dragenter","dragover"].forEach(eventName => {

    dropArea.addEventListener(eventName, e => {

        e.preventDefault();

        dropArea.classList.add("highlight");

    });

});

["dragleave","drop"].forEach(eventName => {

    dropArea.addEventListener(eventName, e => {

        e.preventDefault();

        dropArea.classList.remove("highlight");

    });

});

dropArea.addEventListener("drop", e => {

    const files = e.dataTransfer.files;

    fileInput.files = files;

    if(files.length > 0){

        fileName.innerText = files[0].name;

    }

});