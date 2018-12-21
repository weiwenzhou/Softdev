list=document.getElementById("thelist");
head=document.getElementById("h");
list.addEventListener("mouseover",function(e){
  console.log(e["target"].innerHTML);
  head.innerHTML=e["target"].innerHTML;
  //what is "h"
})
list.addEventListener("mouseout",function(e){
  console.log(e);
  head.innerHTML="Hello world!";
})
