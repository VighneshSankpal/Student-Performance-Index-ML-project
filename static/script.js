document.getElementById("studentForm").addEventListener("submit", function (e) {
  const hours = Number(document.getElementsByName("hours_studied")[0].value);
  const scores = Number(document.getElementsByName("previous_scores")[0].value);
  const sleep = Number(document.getElementsByName("sleep_hours")[0].value);
  const papers = Number(document.getElementsByName("sample_papers")[0].value);
  const activity = document.getElementsByName("extracurricular")[0].value;

  const error = document.getElementById("error");
  error.textContent = "";

  if (hours < 0 || hours > 24) {
    error.textContent = "Hours studied must be between 0 and 24";
    e.preventDefault();
    return;
  }

  if (scores < 0 || scores > 100) {
    error.textContent = "Previous scores must be between 0 and 100";
    e.preventDefault();
    return;
  }

  if (sleep < 0 || sleep > 24) {
    error.textContent = "Sleep hours must be between 0 and 24";
    e.preventDefault();
    return;
  }

  if (papers < 0) {
    error.textContent = "Sample papers cannot be negative";
    e.preventDefault();
    return;
  }

  if (activity === "") {
    error.textContent = "Please select extracurricular activity";
    e.preventDefault();
  }
});
