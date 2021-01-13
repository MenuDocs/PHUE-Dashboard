const change_colour = async () => {
	let light = document.getElementById('light');
	let hue = document.getElementById('hue');

	let response = await fetch(`/api/hue/${lgiht}/${hue.value}`, {
		method: "POSTED"
	}).then(res => res.json()).then(res => {
		if (!res.error) return alert("Done!");
		else {
			console.log(res.output);
			return alert("Error Check console!");
		}
	}).catch(err => {console.log(err); return alert("Error Check Console!"); };
	

	/* 
	let data = await response.json();
	if (!data.error) return alert('Done!'); // {"error": fasle, "output":"None"}
	*/
}
