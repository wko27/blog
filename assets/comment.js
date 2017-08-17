// Submit a comment for the given post
function submitComment(post) {
  var name = document.getElementById("name").value || "anonymous";
  var comment = document.getElementById("comment").value;
  var to = "wko27code@gmail.com";
  console.log("post is: " + post);
  var subject = "[blog-comment]:" + post;
  // base64 encode message body
  var body = btoa(name + ":\n" + comment);
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
    var url = button.getAttribute("data-pageurl");
    console.log("url is: " + url);
    submitComment(url);
  }, false);
};