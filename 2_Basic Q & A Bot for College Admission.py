class CollegeAdmissionBot:
    def __init__(self):
        self.memory = {}
        self.responses = {
            "admission procedure": "The admission procedure involves the following steps:\n"
                                   "1. Submit an online application form.\n"
                                   "2. Provide high school transcripts and standardized test scores.\n"
                                   "3. Attend an interview if required.\n"
                                   "4. Submit letters of recommendation.\n"
                                   "5. Wait for the admission decision, which will be communicated via email or mail.",
            "admission requirements": "The requirements for admission include:\n"
                                      "1. A completed application form.\n"
                                      "2. High school transcripts.\n"
                                      "3. Standardized test scores (e.g., SAT or ACT).\n"
                                      "4. Letters of recommendation.\n"
                                      "5. A personal statement or essay.\n"
                                      "6. Application fee or fee waiver if eligible.",
            "application deadline": "The application deadlines are as follows:\n"
                                    "1. Early Decision: December 1st.\n"
                                    "2. Regular Decision: March 1st.\n"
                                    "3. Transfer Applications: June 1st for the fall semester and November 1st for the spring semester.",
            "tuition fees": "The tuition fees for the upcoming academic year are $20,000 per semester. This does not include additional costs such as room, board, and books.",
            "scholarships": "We offer several scholarships based on merit and financial need. To apply, submit the scholarship application by February 15th. Scholarships include:\n"
                            "1. Merit-based scholarships.\n"
                            "2. Need-based financial aid.\n"
                            "3. Scholarships for specific programs or achievements."
        }
        self.default_response = "I'm sorry, I didn't understand that. Can you please rephrase? You can ask about admission procedures, requirements, deadlines, tuition fees, or scholarships."
        self.farewell_message = "Goodbye! If you have more questions, feel free to ask anytime."
        self.previous_queries = []

    def greet(self):
        return "Hello! I'm your college admission assistant. How can I help you today?"
    
    def farewell(self):
        return self.farewell_message
    
    def respond(self, user_input):
        user_input = user_input.lower().strip()
        self.previous_queries.append(user_input)
        
        for key, response in self.responses.items():
            if key in user_input:
                self.memory[user_input] = response
                return response
        
        response = self.handle_variations(user_input)
        if response:
            self.memory[user_input] = response
            return response
        
        suggestions = self.suggest_possible_queries(user_input)
        return f"{self.default_response} Did you mean: {', '.join(suggestions)}?"
    
    def handle_variations(self, user_input):
        patterns = {
            "admission procedure": ["admission process", "how to apply", "application process", "steps to apply"],
            "admission requirements": ["requirements", "what do I need to apply", "application requirements", "application needs"],
            "application deadline": ["deadline", "when to apply", "application due date", "application cutoff"],
            "tuition fees": ["tuition", "cost", "fees", "how much is tuition"],
            "scholarships": ["scholarships", "financial aid", "grants", "scholarship opportunities"]
        }
        
        for key, keywords in patterns.items():
            if any(keyword in user_input for keyword in keywords):
                return self.responses[key]
        
        return None
    
    def suggest_possible_queries(self, user_input):
        possible_queries = [key for key in self.responses.keys() if key in user_input]
        if not possible_queries:
            possible_queries = list(self.responses.keys())
        return possible_queries[:3]
    
    def remember_interaction(self, user_input, user_response):
        self.memory[user_input] = user_response
    
    def recall_context(self):
        if self.memory:
            context = "Here's what I remember from our conversation: "
            context += " ".join([f"{key.capitalize()} is {value}." for key, value in self.memory.items()])
            return context
        return "I don't have any previous interactions recorded."
    
    def fetch_realtime_info(self, query):
        backend_data = {
            "latest news": "The latest admission news: Applications are up 10% this year!",
            "campus events": "Upcoming event: Open House on September 15th."
        }
        return backend_data.get(query.lower(), "I'm sorry, I don't have that information at the moment.")
    
    def handle_interaction(self):
        print(self.greet())
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "bye":
                print(self.farewell())
                break
            elif user_input.lower() == "recall":
                print(self.recall_context())
            elif user_input.lower().startswith("get info"):
                query = user_input[8:].strip()
                print(self.fetch_realtime_info(query))
            else:
                response = self.respond(user_input)
                print(response)
                self.remember_interaction(user_input, response)

chatbot = CollegeAdmissionBot()
chatbot.handle_interaction()
