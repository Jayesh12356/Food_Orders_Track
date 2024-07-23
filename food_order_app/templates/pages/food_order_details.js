document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('fetch-orders').addEventListener('click', function() {
        var selectedMonth = document.getElementById('month').value;

        // Fetch CSRF token from meta tag or cookies
        // const csrfToken = document.querySelector('meta[name="csrf-token"]') 
        //                     ? document.querySelector('meta[name="csrf-token"]').getAttribute('content')
        //                     : ''; // Or use a function to get it from cookies if necessary

        fetch(`/api/method/food_order_app.api.process_food_orders?month=${selectedMonth}`)
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                let orders = data.message;
                let totalFine = 0;
                let html = "<table class='table'><thead><tr><th>Date</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th><th>Fine</th></tr></thead><tbody>";

                orders.forEach(function(order) {
                    html += `<tr>
                                <td>${order.date}</td>
                                <td>${order.breakfast_status}</td>
                                <td>${order.lunch_status}</td>
                                <td>${order.dinner_status}</td>
                                <td>${order.fine} Rs</td>
                            </tr>`;
                    totalFine += order.fine;
                });

                html += "</tbody></table>";
                document.getElementById('food-orders').innerHTML = html;
                document.getElementById('total-fine').innerText = totalFine;
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
