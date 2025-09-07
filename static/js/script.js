// Update slider value display
function updateValue(slider) {
  const display = document.getElementById(`${slider.id}_val`);
  display.innerText = slider.value;
}

// Initialize all values on page load
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('input[type="range"]').forEach(slider => {
    updateValue(slider);
  });
});
