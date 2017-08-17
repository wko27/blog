// Submit a comment for the given post
function submitComment(postid) {
  var name = document.getElementById("name").value || "anonymous";
  var comment = document.getElementById("comment").value;
  var to = "wko27code@gmail.com";
  var subject = encodeURIComponent("[blog-comment]:" + postid);
  var body = encodeURIComponent(name + ":\n" + comment);
  var gmail = "mailto:" + to + "?subject=" + subject + "&body=" + body;
  window.open(gmail, '_blank');
}

// Set a click event handler for the button
window.onload = function() {
  var button = document.getElementById("button");
  if (!button) {
    return;
  }
  
  button.addEventListener("click", function() {
    var postid = button.getAttribute("data-postid");
    submitComment(postid);
  }, false);
};