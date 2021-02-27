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
		alert(id);
		let api_status=api_link+"api/getStatus/?id="+id;
		let status_response=await fetch(api_status);
		if(status_response.ok){
			let status_text=await status_response.text();
			status_text=status_text.split(":",2);
			let status=status_text[1][1];
			if(status=='-')
				status="-1";
			if(status=='0')
			{
				while(status!='1')
				{
					status_text=await status_response.text();
					status_text=status_text.split(":",2);
					status=status_text[1][1];
				}
			}
			document.write("status is "+status+"<br>");
		}
	}
	else{
		document.write("HTTPS-Error: "+response.status)
	}
	
}
