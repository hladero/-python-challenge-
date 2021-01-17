import csv
import os

#Store data in variables
Pypoll_csv = 'election_data.csv'
Column_name_Voterid = 'Voter_id'
Column_name_County = 'County'
Column_name_Candidate ='Candidate'

def get_filename_csv():
    dirfolder = os.path.dirname(__file__)
    filename = os.path.join(dirfolder, 'Resources/' + Pypoll_csv)
    return filename

def calculate_total_votes_count():

    Pypoll_csv = get_filename_csv()
    #1.2 Read trough the file
    votes_count = 0 
    with open(Pypoll_csv, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')

        #1.2.1 loop to count the number of votes 
            #row [0] is the first column --> Voter id
        lines = 0
        for row in csv_reader:
            if lines > 0: 
                votes_count +=1
            lines +=1
    #1.3 Return the result
    return votes_count


def list_candidates_with_votes():

    Pypoll_csv = get_filename_csv()
    
    #2.2 Read trough the file and extract candidates names
    list_candidates = []
    
    with open (Pypoll_csv, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        #1.2.1 loop trough the candidates and count the candidates with votes count the number of votes 
        lines = 0
        for row in csv_reader:
            if lines > 0: 
                candidate_name = row [2]
                if candidate_name not in list_candidates:
                    list_candidates.append(candidate_name)
            lines +=1
                #candidates_with_votes = candidates_with_votes + str(row[1])+str(row[2])
            lines +=1

    #2.3 Return the result
    return list_candidates

def calculate_total_votes_by_candidate(candidate_to_calculate):

    Pypoll_csv = get_filename_csv()
    
    #3.2 Read trough the file
    votes_cont = 0

    with open (Pypoll_csv, mode = 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')

        lines = 0
        for row in csv_reader:
            if lines > 0:
                candidate_name = row [2]
                if candidate_name == candidate_to_calculate:
                    votes_cont = votes_cont + 1
            lines +=1

    #3.3 Return the result
    return votes_cont


def calculate_percentage_votes_of_each_candidate(candidate_votes, total_votes):

    return (candidate_votes/total_votes)*100

def calculate_winner(dict_candidate_by_votes):

    winner = ''
    max_votes = 0
    for candidate in dict_candidate_by_votes:
        cotes_candidate = dict_candidate_by_votes[candidate]
        if cotes_candidate > max_votes:
            winner = candidate
            max_votes = cotes_candidate

    return winner
    

if __name__ == '__main__':
    
    """ 
        Main is the start of the script
    """

    with open(Pypoll_csv, "w") as txt_file:
        
    # Election Results
    # -------------------------
    # Total
    # Votes: 3521001
    # -------------------------
    # Khan: 63.000 % (2218231)
    # Correy: 20.000 % (704200)
    # Li: 14.000 % (492940)
    # O
    # 'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------

        print("Election Results")
        print("----------------------------")
        print("Total")
    # 1. The total number of votes cast
        total_votes = calculate_total_votes_count()
        print("Votes : {}".format(total_votes))
        print("----------------------------")

    # 2. A complete list of candidates who received votes
        candidates = list_candidates_with_votes()

    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
        dict_candidate_votes = {} 
        for candidate in candidates:
            total_votes_by_candidate = calculate_total_votes_by_candidate(candidate)
            percentage_votes_by_candidate = calculate_percentage_votes_of_each_candidate(total_votes_by_candidate, total_votes)
            print("{}: {:.3f}% ({})".format(candidate, percentage_votes_by_candidate, total_votes_by_candidate))
            dict_candidate_votes.update({candidate: total_votes_by_candidate})

    # 5. The winner of the election based on popular vote.
        print("----------------------------")
        winner = calculate_winner(dict_candidate_votes)
        print("Winner: {}".format(winner))
        print("----------------------------")

