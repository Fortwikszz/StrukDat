class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.next = []
        self.before = []

    def visit(self, url: str) -> None:
        self.before.append(self.current)
        self.current = url
        self.next = []    

    def back(self, steps: int) -> str:
        while steps > 0 and self.before:
            self.next.append(self.current)
            self.current = self.before.pop()
            steps -= 1
        return self.current
        
    def forward(self, steps: int) -> str:
        while steps > 0 and self.next:
            self.before.append(self.current)
            self.current = self.next.pop()
            steps -= 1
        return self.current