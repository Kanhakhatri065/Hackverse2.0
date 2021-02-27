/* 
	Team: Babayaga
	Designed By: Pankaj Kumar.
-*/
async function js_function(){
	let repo_link=document.getElementById('github_link').value;
	let api_link="https://distributed-compiler.herokuapp.com/";
	let api_repo_link= api_link+"api/add/?link="+repo_link;

	// pageloader code
	let code="<style type='text/css'>body{ text-decoration:none; margin: 0px;padding: 0px;background-color: #34495e;height:100vh;display: flex;align-items: center;justify-content: center;font-family: 'montserrat',sans-serif;}.loading{width: 200px;	height:200px;	box-sizing: border-box;	border-radius: 50%;	border-top:10px solid #e74c3c;	position: relative;	animation: al 2s linear infinite;}.loading::before,.loading::after{	content: '';	width:200px;	height: 200px;	position: absolute;	left:0px;	top:-10px;	box-sizing: border-box;	border-radius: 50%;}.loading::before{border-top: 10px solid #e67e22;transform: rotate(120deg);} .loading::after{border-top: 10px solid #3498db;	transform: rotate(240deg);}.loading span{position: absolute;width: 200px;height: 200px;color:#fff;line-height: 200px;text-align: center;	animation: a2 2s linear infinite; }@keyframes al{to{transform: rotate(360deg);}}@keyframes a2{to{transform: rotate(-360deg);}}</style><body><div class='loading'><span>Loading.....</span></div></body>";

	// document.getElementById("root").innerHTML="hello";
	document.open();
	document.write(code);




	let response = await fetch(api_repo_link);

	

	if(response.ok){
		document.close();


		document.open();
		document.write("<style type='text/css'>button a{height: 42px;	width: 155px;font-size: 17px;cursor: pointer;font-weight: bold;background-color: #28a745;	color: white;	border: 1px solid #28a745;top: 50%;	position: absolute;	left: 50%;transform: translate(-50%,-50%);border-radius: 9px;}</style><body><div id='btn'><button><a href='google.com'>Download Link</a></button></div></body>");
		
		var x=document.getElementById('btn')[0];
		document.write(x);
		let data=await response.json();
		let id=data['id'];
		let node_value=data['node'];
		

		let fetch_url=api_link+"api/fetch/?user="+id+"&node="+node_value;
		let second_response=await fetch(fetch_url);
		if(second_response.ok){
			let fetch_data=await second_response.json();
			let code=fetch_data['code'];
			while(code!=0){
				second_response=await fetch(fetch_url);
				fetch_data=await second_response.json();
				code=fetch_data['code'];
				// document.write("document "+code);
			}
			let download_link=fetch_data['down'];
			// document.write("<style type=ext/css'>button{height: 42px;	width: 155px;font-size: 17px;cursor: pointer;font-weight: bold;background-color: #28a745;	color: white;	border: 1px solid #28a745;top: 50%;	position: absolute;	left: 50%;transform: translate(-50%,-50%);border-radius: 9px;}</style><body><div><button class="">Download Link</button></div></body>");
		}
		else{
			document.write("HTTPS-Error2 "+"<br")
		}
	}
	// else{
	// 	document.write("HTTPS-Error: "+response.status)
	// }
}