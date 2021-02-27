/* 
	Team: Babayaga
	Designed By: Pankaj Kumar.
-*/
async function js_function(){
	let repo_link=document.getElementById('github_link').value;
	let api_link="https://distributed-compiler.herokuapp.com/";
	let api_repo_link= api_link+"api/add/?link="+repo_link;

	document.write("");
	let response = await fetch(api_repo_link);

	

	if(response.ok){
		let data=await response.json();
		let id=data['id'];
		let node_value=data['node'];
		// document.write("node is "+node_value+"<br>");
		// document.write(api_repo_link+"<br>");
		// document.write("id is "+id+"<br>");
		

		let fetch_url=api_link+"api/fetch/?user="+id+"&node="+node_value;
		// document.write("fetch url is:  "+fetch_url+"<br>");
		let second_response=await fetch(fetch_url);
		if(second_response.ok){
			let fetch_data=await second_response.json();
			let code=fetch_data['code'];
			document.write("code is "+code+"<br>");
			while(code!=0){
				second_response=await fetch(fetch_url);
				fetch_data=await second_response.json();
				code=fetch_data['code'];
				// document.write("document "+code);
			}
			let download_link=fetch_data['down'];
			document.write("download_link is "+download_link+"<br>");
		}
		else{
			document.write("HTTPS-Error2 "+"<br")
		}
	}
	// else{
	// 	document.write("HTTPS-Error: "+response.status)
	// }
}