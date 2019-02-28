import logging
import os
import fileinput
import sys


# Debugging format.
DEBUG_FORMAT = '%(levelname)s:%(filename)s:%(funcName)s:%(asctime)s %(message)s\n'

# Main method
def main():
    logging.debug("Debug enabled! :)")
    
    # Meta-data input
    a = fileinput.input(sys.argv[1])
    num_rows, num_col, num_vehicle, num_rides, bonus, simstep = map(int, a.readline().rstrip().split(" "))

    # Data input
    rides = []
    cars = []

    # Create car objects
    for i in range(num_vehicle):
        cars.append(Car(i))

    # Create map object
    sim_map = Map(num_rows, num_col)

    # Read in the different rides
    for i in range(num_rides):
        start_row, start_col, end_row, end_col, earliest_start, late_finish = map(int,a.readline().rstrip().split(" "))
        logging.debug("ride {}, {}, {}, {}, {}, {}".format(start_row, start_col, end_row, end_col, earliest_start, late_finish))
        rides.append(Ride(i, start_row, start_col, end_row, end_col, earliest_start, late_finish))

    solver = IterativeSolver(rides, cars, sim_map, bonus, simstep)
    solver.solve()

    # Write away solution!
    output_name = '{}.out'.format(sys.argv[1].split('/')[-1].split('.in')[0])
    SolutionWriter.write_solution('./dist/{}'.format(output_name), cars)

# Entry point of the application.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <dataset>'.format(sys.argv[0]))
        sys.exit(1)

    # Check if DEBUG mode is on or not.
    if "DEBUG" not in os.environ.keys() or os.environ["DEBUG"] == "True":

        # Debug setup to stdout and log file.
        logging.basicConfig(level=logging.DEBUG)
        log_formatter = logging.Formatter(DEBUG_FORMAT)
        root_logger = logging.getLogger()

        file_handler = logging.FileHandler("debug.log", mode='w')
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)

    # Execute the main function.
    main()