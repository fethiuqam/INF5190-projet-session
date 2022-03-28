const rechercheForm = document.getElementById('rechercheForm');
const rechercheInput = document.getElementById('rechercheInput');

function chercherInstallationsParArrondissement(event) {
    event.preventDefault();
    let value = rechercheInput.value.trim();
    if (value.length == 0) {
        setError(rechercheInput, "Ce champ est requis.");
    } else {
        fetch('/api/installations?arrondissement=' + value).then(res => {
            if (res.status === 200) {
               return res.json();
            }
            throw Error
        }).then(installations => {
            let liste = document.createElement("ul");
            installations.forEach(inst => {
                let item = document.createElement('li');
                item.innerText = inst;
                liste.append(item);
            })
            document.body.append(liste);
        }).catch(e => {
            console.log('Erreur: ', e);
        })
    }
}

function setError(formControl, errorMessage) {
    const errorSpan = formControl.parentElement.querySelector('.error');
    errorSpan.style.visibility = 'visible'
    errorSpan.innerHTML = errorMessage
    formControl.className = 'form-control is-invalid'
}

rechercheForm.addEventListener('submit', chercherInstallationsParArrondissement);