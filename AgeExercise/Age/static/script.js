function hideShow(){
    var x = document.getElementById('past');
  if (x.style.display === 'none') {
    x.style.display = 'block';
  } else {
    x.style.display = 'none';
  }
  changeButton()
}

function changeButton(){
  var x = document.getElementById('buttonShow').innerText
  if (x == 'View Deleted People'){
    document.getElementById('buttonShow').innerText = 'Hide Deleted People';
  } else {
    document.getElementById('buttonShow').innerText = 'View Deleted People';
  }

}