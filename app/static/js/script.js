/* static/js/script.js */
document.addEventListener('DOMContentLoaded', function () {
  var predictButton = document.getElementById('predictButton');
  var predictForm = document.getElementById('predictForm');

  predictButton.addEventListener('click', function (event) {
    event.preventDefault();  // Prevent the default form submission behavior

    // Simulate form submission
    predictForm.submit();
  });

  // Function to open the prediction modal
  window.displayPrediction = function (predictionText) {
    var modal = document.getElementById('predictionModal');
    var predictionOutput = document.getElementById('predictionText');

    predictionOutput.innerHTML = predictionText;
    modal.style.display = 'block';
  };

  // Function to close the prediction modal
  window.closeModal = function () {
    var modal = document.getElementById('predictionModal');
    modal.style.display = 'none';
  };
});
