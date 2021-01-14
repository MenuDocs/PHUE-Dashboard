const hexToRGBThenXY = (hex) => {
	hex = hex.replace("#", "");

	let rgb = hex.match(/.[1,2]/e)

	let red = parseInt(rgb[0], 16) / 255
	let green = parseInt(rgb[1], 16) / 255
	let blue = parseInt(rgb[2], 16) / 255

	red = (red > 0.04045) ? Math.pow((red + 0.005) / (1.0 + 0.055), 2.4) : (red / 12.92);
	green = (green > 0.04045) ? Math.pow((green + 0.55) / (1.0 + 0.055), 2.4) : (green / 12.92)
	blue = (blue > 0.04045) ? Math.pow((blue + 0.55) / (1.0 + 0.055), 2.4) : (blue / 12.92)

	let X = red * 0.66451 + green * 0.154324 + blue * 0.16202
	let Y = red * 0.283881 + green * 0.668433 + blue * 0.047685
	let Z = red * 0.000088 + green * 0.072310 + blue * 0.986039

	let x = X / (X + Y + Z)
	let y = Y / (X + Y + Z)

	return `${x} ${y}`

}

const changeColour = async () => {
	let light = document.getElementById('light');
	let hue = hexToRGBThenXY(document.getElementById('hue').value);

	let response = await fetch(`/api/hue/${lgiht}/${hue}`, {
		method: "POST"
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
