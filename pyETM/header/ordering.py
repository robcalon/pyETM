class Ordering:
    
    @property
    def ordering(self):
        
        # get scenario header
        if self._scenario_header is None:
            self._get_scenario_header()
        
        return self._scenario_header['ordering']