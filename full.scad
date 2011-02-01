


module arms(){
	rotate(90,[0,1,0])
	rotate(-90,[1,0,0])
	translate([-97,-60,118])
	dxf_linear_extrude(file = "parts.dxf", layer = "arm" ,height = 6, center = true, convexity = 20);

	rotate(90,[0,1,0])
	rotate(-90,[1,0,0])
	translate([-97,-60,-118])
	dxf_linear_extrude(file = "parts.dxf", layer = "arm" ,height = 6, center = true, convexity = 20);

	translate([60,-125,97])
	rotate(90,[0,1,0])
	//rotate(-90,[1,0,0])
	dxf_linear_extrude(file = "parts.dxf", layer = "armsupport" ,height = 6, center = true, convexity = 20);

	translate([60,125,97])
	rotate(90,[0,1,0])
	rotate(-180,[1,0,0])
	dxf_linear_extrude(file = "parts.dxf", layer = "armsupport" ,height = 6, center = true, convexity = 20);
}

module cam_mount()
{
	rotate(90,[1,0,0])
	translate([204,-103,125])
	rotate(90,[0,1,0]){
		dxf_linear_extrude(file = "parts.dxf", layer = "cam_clamp" ,height = 6, center = true, convexity = 20);
		translate([0,0,6])
		dxf_linear_extrude(file = "parts.dxf", layer = "cam_front" ,height = 6, center = true, convexity = 20);
	}
	
}

module bed(){
	dxf_linear_extrude(file = "parts.dxf", layer = "bed" ,height = 6, center = true, convexity = 10);
}

module bearing_holders(){
	module bearing_holder(){
		translate([-71,0,0])
		rotate(-90,[0,1,0])
		{
			translate([3,0,0])
			dxf_linear_extrude(file = "parts.dxf", layer = "bearing_h" ,height = 6, center = true, convexity = 10);
			translate([3,0,16])
			dxf_linear_extrude(file = "parts.dxf", layer = "bearing_h" ,height = 6, center = true, convexity = 10);
			translate([17,0,8])
			dxf_linear_extrude(file = "misc.dxf", layer = "bearing" ,height = 6, center = true, convexity = 10);
			translate([17,0,-5])
			dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale=10);
			translate([17,0,21])
			dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale=10);

		}
	}
	bearing_holder();
	rotate(120,[0,0,1])
		bearing_holder();
	rotate(-120,[0,0,1])
		bearing_holder();
}

module platform(){
	
	//The under platform
	translate([0,0,22])
	dxf_linear_extrude(file = "parts.dxf", layer = "platform2" ,height = 6, center = true, convexity = 10);
	
	//The main platform
	translate([0,0,28])
	dxf_linear_extrude(file = "parts.dxf", layer = "platform1" ,height = 6, center = true, convexity = 10);
	
	//The Bearing
	dxf_linear_extrude(file = "misc.dxf", layer = "bearing" ,height = 6, center = true, convexity = 10);
	
	//The base bearing holder
	translate([0,0,-6])
	dxf_linear_extrude(file = "parts.dxf", layer = "bedbearing_h" ,height = 6, center = true, convexity = 10);
	
	//The Gear
	translate([0,0,16])
	dxf_linear_extrude(file = "parts.dxf", layer = "gear1" ,height = 6, center = true, convexity = 10);
	
	//The Second gear
	translate([-36,-36,16])
	dxf_linear_extrude(file = "parts.dxf", layer = "gear2" ,height = 6, center = true, convexity = 10);		

	//The Nuts
	translate([0,0,-6])
	dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale = 10);
	translate([0,0,5])
	dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale = 10);
	translate([0,0,11])
	dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale = 10);
	translate([0,0,28])
	dxf_linear_extrude(file = "misc.dxf", layer = "nut" ,height = 5, center = true, convexity = 10,scale = 10);
}


module laserholder(){
	translate([110,110,3])	
	rotate(90,[1,0,0])
	rotate(45,[0,1,0])
	{
		dxf_linear_extrude(file = "parts.dxf", layer = "laserholder1" ,height = 6, center = true, convexity = 10);
		rotate(90,[0,1,0])
		translate([0,0,-33])
		dxf_linear_extrude(file = "parts.dxf", layer = "laserholder2" ,height = 6, center = true, convexity = 10);
		rotate(90,[1,0,0])
		rotate(90,[0,0,1])
		translate([0,10,-63])
		dxf_linear_extrude(file = "parts.dxf", layer = "laserholder3" ,height = 6, center = true, convexity = 10);
	}
}

module case(){
	rotate(90,[1,0,0]){
		translate([-125,-103,0]){
			translate([0,0,-128])
			dxf_linear_extrude(file = "parts.dxf", layer = "side" ,height = 6, center = true, convexity = 20);
			translate([0,0,128])
			dxf_linear_extrude(file = "parts.dxf", layer = "side" ,height = 6, center = true, convexity = 20);
			translate([253,0,125])
			rotate(90,[0,1,0])
			dxf_linear_extrude(file = "parts.dxf", layer = "front" ,height = 6, center = true, convexity = 20);
			translate([259,0,125])
			rotate(90,[0,1,0])
			dxf_linear_extrude(file = "parts.dxf", layer = "frontclamp" ,height = 6, center = true, convexity = 20);
			translate([-3,0,125])
			rotate(90,[0,1,0])
			dxf_linear_extrude(file = "parts.dxf", layer = "back" ,height = 6, center = true, convexity = 20);
			

		}
	}
	translate([0,0,200])
	dxf_linear_extrude(file = "parts.dxf", layer = "top" ,height = 6, center = true, convexity = 20);
	translate([0,0,-106])
	dxf_linear_extrude(file = "parts.dxf", layer = "top" ,height = 6, center = true, convexity = 20);
}

/*******************Drawing the scanner********************/
//$fa = 1;
//$fs = 0.01;
bearing_holders();
case();
platform();
laserholder();
arms();
bed();
cam_mount();


/*translate([60,113,98])
rotate(90,[0,1,0])
rotate(-90,[1,0,0])
dxf_linear_extrude(file = "parts.dxf", layer = "arm" ,height = 6, center = true, convexity = 20);
translate([60,-113,98])
rotate(90,[0,1,0])
rotate(-90,[1,0,0])
dxf_linear_extrude(file = "parts.dxf", layer = "arm" ,height = 6, center = true, convexity = 20);

translate([0,-125,98])
rotate(90,[0,1,0])
//rotate(-90,[1,0,0])
dxf_linear_extrude(file = "parts.dxf", layer = "armsupport" ,height = 6, center = true, convexity = 20);

translate([0,125,98])
rotate(90,[0,1,0])
rotate(-180,[1,0,0])
dxf_linear_extrude(file = "parts.dxf", layer = "armsupport" ,height = 6, center = true, convexity = 20);*/
