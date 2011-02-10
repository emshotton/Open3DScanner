//This work is under a creative commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) License
//for more details see: http://creativecommons.org/licenses/by-nc-sa/3.0/
//By matt shotton
//matthewshotton.wordpress.com

module laserholder(){
	translate([115,115,3])	
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

module case(){
	rotate(90,[1,0,0])
	translate([0,0,133])
	dxf_linear_extrude(file = "parts.dxf", layer = "front" ,height = 6, center = true, convexity = 10);
	rotate(90,[1,0,0])
	translate([0,0,-133])
	dxf_linear_extrude(file = "parts.dxf", layer = "back" ,height = 6, center = true, convexity = 10);
	translate([0,0,206])
	dxf_linear_extrude(file = "parts.dxf", layer = "top" ,height = 6, center = true, convexity = 10);

	rotate(90,[0,0,1])
	rotate(90,[1,0,0])
	translate([0,0,-133])
	dxf_linear_extrude(file = "parts.dxf", layer = "side" ,height = 6, center = true, convexity = 10);
	rotate(90,[0,0,1])
	rotate(90,[1,0,0])
	translate([0,0,293])
	dxf_linear_extrude(file = "parts.dxf", layer = "side" ,height = 6, center = true, convexity = 10);
}

module cam_mount(){
	rotate(90,[1,0,0])
	translate([245,0,97])
	dxf_linear_extrude(file = "parts.dxf", layer = "cam_strut" ,height = 6, center = true, convexity = 10);
	rotate(90,[1,0,0])
	translate([245,0,-97])
	dxf_linear_extrude(file = "parts.dxf", layer = "cam_strut" ,height = 6, center = true, convexity = 10);

}

/*******************Drawing the scanner********************/
//$fa = 1;
//$fs = 0.01;
bearing_holders();
platform();
laserholder();
%bed();
%case();
cam_mount();
