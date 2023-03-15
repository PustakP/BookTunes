// Show the spinner when the form is submitted
document.getElementById("my-form").addEventListener("submit", function() {
  document.getElementById("loading-spinner").style.display = "block";
});

// Hide the spinner when the page finishes loading
window.addEventListener("load", function() {
  document.getElementById("loading-spinner").style.display = "none";
});
