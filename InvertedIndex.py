import re
# import gui as g     **creates a circular dependancy! do not un comment.

class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """
    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency        
    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)



class Database:
    """
    In memory database representing the already indexed documents.
    """
    def __init__(self):
        self.db = dict()
    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.__dict__)    
    def get(self, id):
        return self.db.get(id, None)    
    def add(self, document):
        """
        Adds a document to the DB.
        """
        return self.db.update({document['id']: document})
    def remove(self, document):
        """
        Removes document from DB.
        """
        return self.db.pop(document['id'], None)


class InvertedIndex:
    """
    Inverted Index class.
    """
    def __init__(self, db):
        self.index = dict()
        self.db = db
    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index) 

    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """
        
        # Remove punctuation from the text.
        clean_text = re.sub(r'[^\w\s]','', document['text'])
        terms = clean_text.split(' ')
        appearances_dict = dict()        

        # Dictionary with each term and the frequency it appears in the text.
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)
            
        # Update the inverted index
        update_dict = { key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items() }

        self.index.update(update_dict)

        # Add the document into the database
        self.db.add(document)

        return document    
    
    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances. 
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return { term: self.index[term] for term in query.split(' ') if term in self.index }


def index_documents(index):
    document1 = {
        'id': '1',
        'text': 'It resides in a cavern on the moon.'
    }    
    document2 = {
        'id': '2',
        'text': 'The lunar brew expedition.'
    }    
    document3 = {
        'id': '3',
        'text': 'beer beer beer!'
    }  
    document4 = {
        'id': '4',
        'text': 'Space travel has changed to way we consume beer.'
    }  
    document5 = {
        'id': '5',
        'text': 'Over the moon brew.'
    }  
    document6 = {
        'id': '6',
        'text': 'Deep in the caverns of the moon, beer.'
    }  
    index.index_document(document1)
    index.index_document(document2)
    index.index_document(document3)
    index.index_document(document4)
    index.index_document(document5)
    index.index_document(document6)

def index_lookup_query(search_term):  
    db = Database()
    index = InvertedIndex(db)
    index_documents(index)
    result = index.lookup_query(search_term)
    for key, value in result.items():
        for appearance in value:
            yield '{}, {}'.format(appearance.docId, appearance.frequency)

def main():
    search_term = input('Enter term to search for: ')
    # 
    # result = index.lookup_query(search_term)


    for line in index_lookup_query(search_term):
        print(line)
    print("-----------------------------")


if __name__ == "__main__":
    main()
