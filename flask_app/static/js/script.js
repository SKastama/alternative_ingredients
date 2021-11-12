function search(e){
    e.preventDefault();
    var searchForm = document.getElementById('searchForm')
    var form = new FormData(searchForm);
    fetch('http://localhost:5000/search',{method:'POST',body:form})
        .then(res => res.json() )
        .then(data => {
            var itemName = document.getElementById('itemName');
            removeAllChildNodes(itemName);
            var message = document.getElementById('message');
            removeAllChildNodes(message);
            var subs = document.getElementById('subs')
            removeAllChildNodes(subs);
            if (data.status == "success") {
                // Item name
                let tableHeader = document.createElement('th');
                tableHeader.innerHTML = `${capitalizeFirstLetter(data.ingredient)} Substitutes`;
                itemName.appendChild(tableHeader);
                // Message
                let tableMessage = document.createElement('p');
                tableMessage.innerHTML = capitalizeFirstLetter(data.message);
                message.appendChild(tableMessage);
                // Substitutes
                for (let i=0; i < data.substitutes.length; i++) {
                    let row = document.createElement('tr');
                    let name = document.createElement('td');
                    name.innerHTML = data.substitutes[i];
                    row.appendChild(name);
                    subs.appendChild(row);
                }
            }
            else {
                let tableMessage = document.createElement('p');
                tableMessage.innerHTML = capitalizeFirstLetter(data.message);
                message.appendChild(tableMessage);
            }
        })
}
function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}