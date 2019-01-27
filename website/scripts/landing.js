function textToggle() {
    var info = document.getElementById("info");
    var textButton = document.getElementById("text-toggle");

    if (textButton.innerHTML === "Read more.") {
        info.innerHTML = "Project monochrome is an image processing software, capable of determining \
        the precise fraction of an image that is light vs dark in color. Applications for this technology \
        extend to the domain of science, where the detection of the slightest change in monochromatic colors \
        can be an indication of more sinister problems such as in the case of X-rays, fractures or tumors. The \
        same technology could be applied to microscopy, where such small scale imaging is necessary to \
        detect defects in a given material.";
        textButton.innerHTML = "Read less."
    } else if (textButton.innerHTML === "Read less.") {
        info.innerHTML = "Project monochrome is an image processing software, capable of determining \
        the precise fraction of an image that is light vs dark in color.";
        textButton.innerHTML = "Read more.";
    }    
}

/*
function loadPage() {
    const form = document.getElementById("image-form");
    form.addEventListener('submit', e => {
        e.preventDefault();
        submitImage(e);
    });
}


function submitImage(event) {
    let file = event.target[0].files[0];
    const formData = new FormData();
    formData.append('file', file);

    const url = 'http://127.0.0.1:5000/process-image';
    let header = new Headers({
        'Access-Control-Allow-Origin':'*',
        'Content-Type': 'multipart/form-data'
    });

    fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        body: formData
    }).then(response => {
        console.log(response);
    }).catch(err => {
        console.error(err);
    });

}
*/
