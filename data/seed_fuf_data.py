"""Utility file to seed unprocessed tree database from Friends of the Urban Forest"""

from fuf_model import Tree, Plot, Specie, connect_to_db, db
from server import app


def load_trees():
    """Load trees into database."""
    print "I'm in load_trees()"
    f = open("small_fuf_trees_trimmed.csv")

    new_line_f = list(f)[0].split('\r') # this is just the whole file for some terrible reason
    for line in new_line_f: #splits into lines
        # print line
        split_line = line.split(',') # split that on commas
        print "split line: %s" % split_line

        new_tree = Tree(tree_id=split_line[0], 
			        	tree_species_id=split_line[2], 
			        	tree_plot_id=split_line[1])
        print new_tree
    #     db.session.add(new_tree)

    # db.session.commit()

def load_species():
    """Load species into database."""
    
    f = open("fuf_species_trimmed.csv")

    for line in f:
        split_line = line.rstrip().split()
        new_species = Specie(species_id=split_line[0], 
			        	scientific_name=split_line[1],
			        	common_name=split_line[2],
			        	fruit_period=split_line[4])
        db.session.add(new_species)

    db.session.commit()

def load_plots():
    """Load plots into database."""
    
    f = open("fuf_plots_trimmed.csv")

    for line in f:
        print "***********************line: %s" % line
        split_line = line.rstrip().split()
        print "***********************split line: %s" % split_line
        new_plot = Plot(plot_id=split_line[1], 
			        	wkt=split_line[0],
			        	address_street=split_line[2],
			        	address_geocoded=split_line[3],
			        	lat_geocoded=split_line[4],
			        	lon_geocoded=split_line[5])
        db.session.add(new_plot)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    load_trees()
    # load_species()
    # load_plots()