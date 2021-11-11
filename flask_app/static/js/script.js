function search(e){
    e.preventDefault();
    var searchForm = document.getElementById('searchForm')
    var form = new FormData(searchForm);
    fetch('http://localhost:5000/search',{method:'POST',body:form})
        .then(res => res.json() )
        .then(data => {
            var subs = document.getElementById('subs')
            for (let i=0; i < data.substitutes.length; i++) {
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data.substitutes[i];
                row.appendChild(name);
                subs.appendChild(row);
            }
        })
        
}
