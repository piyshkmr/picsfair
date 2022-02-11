function setImageToModal(image) {
  console.log(image);
  document.getElementById("previewImage").src = image;
  document.getElementById("downloadBtn").href = image;
  document.getElementById("previewBtn").href = image;
}
