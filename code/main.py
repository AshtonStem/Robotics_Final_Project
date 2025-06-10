# Seeder Bot Code - Grade 8
# This robot moves like a farmer and drops seeds

from vex import *

# Set up the brain and motors
brain = Brain()

# Motors for driving
left_motor = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)  # reversed

# Seeder motor
seeder = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)

# Set up the drivetrain
drivetrain = DriveTrain(left_motor, right_motor, 319.19, 292.1, DistanceUnits.MM)

# Start of program
brain.screen.print("Starting Seeder Bot")

# First row
drivetrain.drive_for(FORWARD, 1000, MM)
seeder.spin_for(FORWARD, 90, DEGREES)
wait(0.5, SECONDS)
seeder.spin_for(REVERSE, 90, DEGREES)

# Turn around
drivetrain.turn_for(LEFT, 180, DEGREES)

# Second row
drivetrain.drive_for(FORWARD, 1000, MM)
seeder.spin_for(FORWARD, 90, DEGREES)
wait(0.5, SECONDS)
seeder.spin_for(REVERSE, 90, DEGREES)

# Turn around again
drivetrain.turn_for(LEFT, 180, DEGREES)

# Third row
drivetrain.drive_for(FORWARD, 1000, MM)
seeder.spin_for(FORWARD, 90, DEGREES)
wait(0.5, SECONDS)
seeder.spin_for(REVERSE, 90, DEGREES)

brain.screen.print("Done Seeding!")
