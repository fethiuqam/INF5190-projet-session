window.addEventListener("load", function () {
    const searchArrondissement = document.getElementById('search-arrondissement');
    const searchInput = document.getElementById('search-input');
    const searchInstallation = document.getElementById('search-installation');

    const results = document.getElementById('results');
    const flashAlert = document.getElementById('flash-alert');

    searchArrondissement.addEventListener('submit', searchInstallationByArrondissement);
    searchInstallation.addEventListener('change', searchInstallationByName);


    function searchInstallationByArrondissement(event) {
        event.preventDefault();
        let value = searchInput.value.trim();
        if (value.length == 0) {
            setError(searchInput, "Ce champ est requis.");
        } else {
            fetch('/api/installations?arrondissement=' + value).then(res => {
                if (res.status === 200) {
                    return res.json();
                }
                throw Error
            }).then(installations => {
                displayResults(installations);
            }).catch(e => {
                displayFlashAlert('Une erreur est survenue lors du chargement des résultats de la recherche.', 'failure');
            })
        }
    }

    function searchInstallationByName() {
        let value = searchInstallation.value;
        if (value.length > 0) {
            fetch('/api/installations?nom=' + value).then(res => {
                if (res.status === 200) {
                    return res.json();
                }
                throw Error
            }).then(installations => {
                displayResults(installations);
            }).catch(e => {
                displayFlashAlert('Une erreur est survenue lors du chargement des résultats de la recherche.', 'failure');
            })
        }
    }


    function displayResults(resultat) {
        const types = ['glissade', 'patinoire', 'piscine'];
        const headers = [headerGlissade, headerPatinoire, headerPiscine];

        results.innerHTML = '';
        if (resultat.length > 0) {
            const installations = []
            for (tp of types) {
                installations.push(resultat.filter((inst) => inst.type === tp));
            }
            for (let i = 0; i < installations.length; ++i) {
                if (installations[i].length > 0) {
                    let title = document.createElement('h2');
                    title.innerText = 'Les ' + types[i] + 's';
                    results.append(title);
                    let table = createTable(installations[i], headers[i]);
                    results.append(table);
                }
            }
        } else {
            results.innerHTML = 'Aucun résultat trouvé';
        }
    }

    function createTable(installations, header) {
        const divResponsive = document.createElement('div');
        divResponsive.className = 'table-responsive';
        const table = document.createElement('table');
        table.className = 'table table-hover';
        divResponsive.append(table);
        const thead = document.createElement('thead');
        thead.innerHTML = header;
        table.append(thead);
        const tbody = document.createElement('tbody');
        installations.forEach(inst => {
            const row = createRow(inst);
            tbody.append(row);
        });
        table.append(tbody)
        return divResponsive;
    }

    const headerGlissade = `<tr><th scope="col">Nom</th>
                            <th scope="col">Arrondissement</th>
                            <th scope="col">Ouvert</th>
                            <th scope="col">Déblayée</th>
                            <th scope="col">Condition</th>
                            <th scope="col">Mise à jour</th>
                            <th scope="col">Actions</th></tr>`;

    const headerPatinoire = `<tr><th scope="col">Nom</th>
                            <th scope="col">Arrondissement</th>
                            <th scope="col">Ouvert</th>
                            <th scope="col">Déblayée</th>
                            <th scope="col">Arrosée</th>
                            <th scope="col">Resurfacée</th>
                            <th scope="col">Mise à jour</th>
                            <th scope="col">Actions</th></tr>`;

    const headerPiscine = `<tr><th scope="col">Nom</th>
                       <th scope="col">Arrondissement</th>                           
                       <th scope="col">Id UEV</th>
                       <th scope="col">Type de piscine</th>
                       <th scope="col">Adresse</th>
                       <th scope="col">Propriété</th>
                       <th scope="col">Gestion</th>
                       <th scope="col">Équipement</th>
                       <th scope="col">Point X</th>
                       <th scope="col">Point Y</th>
                       <th scope="col">Longitude</th>
                       <th scope="col">Latitude</th>
                       <th scope="col">Actions</th></tr>`;

    function createRow(inst) {
        let row = document.createElement('tr');
        updateRow(row, inst)
        return row;
    }

    function updateRow(row, inst) {
        row.setAttribute('data-object', JSON.stringify(inst))
        row.innerHTML = `<th>${inst.nom}</th>
                        <td>${inst.arrondissement}</td>`;
        if (inst.type === 'glissade') {
            row.innerHTML += `<td>${displayBooleanNull(inst.ouvert)}</td>
                            <td>${displayBooleanNull(inst.deblaye)}</td>
                            <td>${inst.condition}</td>
                            <td>${displayDate(inst.mise_a_jour)}</td>`;
        } else if (inst.type === 'patinoire') {
            row.innerHTML += `<td>${displayBooleanNull(inst.ouvert)}</td>
                            <td>${displayBooleanNull(inst.deblaye)}</td>
                            <td>${displayBooleanNull(inst.arrose)}</td>
                            <td>${displayBooleanNull(inst.resurface)}</td>
                            <td>${displayDate(inst.mise_a_jour)}</td>`;
        } else {
            row.innerHTML += `<td>${inst.id_uev}</td>
                         <td>${inst.type_piscine}</td>
                         <td>${inst.adresse}</td>
                         <td>${inst.propriete}</td>
                         <td>${inst.gestion}</td>
                         <td>${inst.equipement}</td>
                         <td>${inst.point_x}</td>
                         <td>${inst.point_y}</td>
                         <td>${inst.longitude}</td>
                         <td>${inst.latitude}</td>`;
        }
        const actions = document.createElement('td');
        actions.append(createButton('Modifier', 'btn btn-outline-success', modifyInstallation));
        actions.append(createButton('Supprimer', 'btn btn-outline-danger', deleteInstallation));
        row.append(actions);
    }

    function displayBooleanNull(value) {
        if (value === null)
            return 'Néant';
        else if (value === true)
            return 'Oui';
        else
            return 'Non';
    }

    function displayDate(value) {
        return new Date(value).toLocaleString('fr-CA');
    }

    function createButton(text, classeName, callback) {
        const button = document.createElement('button');
        button.className = classeName;
        button.innerText = text;
        button.addEventListener('click', callback);
        return button;
    }

    function modifyInstallation(event) {
        const row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        row.innerHTML = `<th>${inst.nom}</th>
                        <td>${inst.arrondissement}</td>`;
        if (inst.type === 'glissade') {
            row.append(createSelectBooleanNull(inst.ouvert));
            row.append(createSelectBooleanNull(inst.deblaye));
            row.innerHTML += `<td><input type="text" class="form-control" value="${inst.condition}"></td>
                          <td><input type="datetime-local" class="form-control" value="${inst.mise_a_jour}"></td>`;
        } else if (inst.type === 'patinoire') {
            row.append(createSelectBooleanNull(inst.ouvert));
            row.append(createSelectBooleanNull(inst.deblaye));
            row.append(createSelectBooleanNull(inst.arrose));
            row.append(createSelectBooleanNull(inst.resurface));
            row.innerHTML += `<td><input type="datetime-local" class="form-control" value="${inst.mise_a_jour}"></td>`;
        } else {
            row.innerHTML += `<td><input type="text" class="form-control" value="${inst.id_uev}"></td>
                              <td><input type="text" class="form-control" value="${inst.type_piscine}"></td>
                              <td><input type="text" class="form-control" value="${inst.adresse}"></td>
                              <td><input type="text" class="form-control" value="${inst.propriete}"></td>
                              <td><input type="text" class="form-control" value="${inst.gestion}"></td>
                              <td><input type="text" class="form-control" value="${inst.equipement}"></td>
                              <td><input type="text" class="form-control" value="${inst.point_x}"></td>
                              <td><input type="text" class="form-control" value="${inst.point_y}"></td>
                              <td><input type="number" class="form-control" value="${inst.longitude}"></td>
                              <td><input type="number" class="form-control" value="${inst.latitude}"></td>`;
        }
        const actions = document.createElement('td');
        actions.append(createButton('Confirmer', 'btn btn-outline-info', saveModification));
        actions.append(createButton('Annuler', 'btn btn-outline-secondary', cancelModification));
        row.append(actions);
        return row;
    }

    function createSelectBooleanNull(value) {
        const td = document.createElement('td');
        td.innerHTML = `<select class="form-control" >
                          <option value="null" ${value === null ? "selected" : ""}  >Néant</option>
                          <option value="true" ${value === true ? "selected" : ""} >Oui</option>
                          <option value="false" ${value === false ? "selected" : ""} >Non</option>
                        </select>`;
        return td;
    }

    function saveModification(event) {
        let row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        const oldInst = Object.assign({}, inst);
        cells = row.children;
        if (inst.type === 'glissade') {
            inst.ouvert = JSON.parse(cells[2].firstChild.value);
            inst.deblaye = JSON.parse(cells[3].firstChild.value);
            inst.condition = cells[4].firstChild.value;
            inst.mise_a_jour = cells[5].firstChild.value;
        } else if (inst.type === 'patinoire') {
            inst.ouvert = JSON.parse(cells[2].firstChild.value);
            inst.deblaye = JSON.parse(cells[3].firstChild.value);
            inst.arrose = JSON.parse(cells[4].firstChild.value);
            inst.resurface = JSON.parse(cells[5].firstChild.value);
            inst.mise_a_jour = cells[6].firstChild.value;
        } else {
            inst.id_uev = parseInt(cells[2].firstChild.value);
            inst.type_piscine = cells[3].firstChild.value;
            inst.adresse = cells[4].firstChild.value;
            inst.propriete = cells[5].firstChild.value;
            inst.gestion = cells[6].firstChild.value;
            inst.equipement = cells[7].firstChild.value;
            inst.point_x = cells[8].firstChild.value;
            inst.point_y = cells[9].firstChild.value;
            inst.longitude = parseFloat(cells[10].firstChild.value);
            inst.latitude = parseFloat(cells[11].firstChild.value);
        }
        const inst_api = Object.assign({}, inst);
        delete inst_api.type;
        delete inst_api.id;
        fetch(`/api/${inst.type}/${inst.id}`, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inst_api)
        }).then(res => {
            if (res.status === 200) {
                displayFlashAlert('La modification s\'est bien déroulée.', 'success');
                row.innerHTML = '';
                updateRow(row, inst);
            } else {
                throw Error();
            }
        }).catch(e => {
            displayFlashAlert('Une erreur est survenue lors de la modification de l\'installation .', 'failure');
            row.innerHTML = '';
            updateRow(row, oldInst);
        });
    }

    function cancelModification(event) {
        const row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);
        row.innerHTML = '';
        updateRow(row, inst);
    }

    function deleteInstallation(event) {
        const row = event.target.parentElement.parentElement;
        const inst = JSON.parse(row.dataset.object);

        fetch(`/api/${inst.type}/${inst.id}`, {
            method: 'DELETE'
        }).then(res => {
            if (res.status === 200) {
                displayFlashAlert('La suppression de l\'installation s\'est bien déroulée.', 'success');
                row.remove();
            } else {
                throw Error();
            }
        }).catch(e => {
            displayFlashAlert('Une erreur est survenue lors de la suppression de l\'installation .', 'failure');
        });
    }

    function displayFlashAlert(msg, type) {
        if (type === 'success') {
            flash = createSuccessAlert(msg);
        } else {
            flash = createFailureAlert(msg);
        }
        flashAlert.append(flash);
        setTimeout(() => flashAlert.removeChild(flashAlert.firstElementChild), 5000);
    }

    function createFailureAlert(msg) {
        const alert = document.createElement('div');
        alert.className = 'alert alert-danger alert-dismissible d-flex align-items-center fade show';
        alert.innerHTML = `<i class="bi-exclamation-octagon-fill"></i>
                           <strong class="mx-2">Erreur !  </strong> ${msg}
                           <button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
        return alert;
    }

    function createSuccessAlert(msg) {
        const alert = document.createElement('div');
        alert.className = 'alert alert-success alert-dismissible d-flex align-items-center fade show';
        alert.innerHTML = `<i class="bi-check-circle-fill"></i>
                           <strong class="mx-2">Succès! </strong> ${msg}
                           <button type="button" class="btn-close" data-bs-dismiss="alert"></button>`;
        return alert;
    }

    function setError(formControl, errorMessage) {
        const errorSpan = formControl.parentElement.querySelector('.error');
        errorSpan.style.visibility = 'visible'
        errorSpan.innerHTML = errorMessage
        formControl.className = 'form-control is-invalid'
    }
});