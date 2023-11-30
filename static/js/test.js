fetch("{% url 'api_address' %}")
  .then(response => response.json())
  .then(data => console.log(data))  