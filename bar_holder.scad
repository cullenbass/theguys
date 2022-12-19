E2E_BAR =53.72;
BAR_HOLE_SIZE = 4.5;
BAR_THICK = 1;
FELT_SIZE = 15;
FELT_THICK = 3;
STAND_BOTTOM = 25;
SCREW_H = 12;
SCREW_D = 2.7;
SOLENOID_HEIGHT = 33;
SOLENOID_STROKE = 6;
THIN_THICK = 1.2;

total_height = SOLENOID_STROKE + THIN_THICK + SOLENOID_HEIGHT - FELT_THICK - .5;

$fn = $preview ? 32: 64;
module stand() {
    screw_d1 = 5.6;
    screw_d2 = 4.8;
    screw_h = SCREW_H;
    difference() {
        cylinder(d=FELT_SIZE, h=total_height);
        combined_thick = screw_h - (BAR_THICK + FELT_THICK);
        translate([0,0,total_height-combined_thick])
        cylinder(d=SCREW_D, h=combined_thick);
    }
}


wall_height = 10;
union() {
    stand();
    translate([E2E_BAR-BAR_HOLE_SIZE,0,0]) {
        stand(); 
        cylinder(h=THIN_THICK, d=STAND_BOTTOM);
    }
    cylinder(h=THIN_THICK, d=STAND_BOTTOM);
    translate([0,(-STAND_BOTTOM)/2,0]) {
        cube([E2E_BAR-BAR_HOLE_SIZE,STAND_BOTTOM, THIN_THICK]);
    }
    if (total_height > 15) {
        translate([0,FELT_SIZE/2-THIN_THICK,wall_height])
        cube([E2E_BAR-BAR_HOLE_SIZE,THIN_THICK, total_height-wall_height]);
    }
}