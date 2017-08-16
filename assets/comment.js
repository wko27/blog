function submitComment(post) {
  var name = document.getElementById("name").value;
  var comment = document.getElementById("comment").value;
  var to = "wko27code@gmail.com";
  var subject = "[blog-comment]:" + post;
  // base64 encode message body
  var body = btoa(name + ":\n" + comment);
  var gmail = "mailto:" + to + "?subject=" + subject + "&body=" + body;
  window.open(gmail, '_blank');
}
