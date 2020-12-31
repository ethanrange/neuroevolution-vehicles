class button():
    
    def __init__(self, x, y, w, h, btnText, mx, my, ac):
        self.pos = PVector(x, y)
        self.dim = PVector(w, h)
        self.textMargin = PVector(mx, my)
        self.text = btnText
        
        self.actionCode = ac
        
    def show(self):
        push()
        rectMode(CORNER)
        if self.actionCode == 'swtr':
            fill(230)
        else:
            fill(250)
        rect(self.pos.x, self.pos.y, self.dim.x, self.dim.y)
        
        noFill()
        stroke(0)
        strokeWeight(4)
        rect(self.pos.x, self.pos.y, self.dim.x, self.dim.y)
        
        fill(0)
        textSize(25)
        text(self.text, self.pos.x+self.textMargin.x, self.pos.y+self.textMargin.y)
        
        pop()
        
    def handleEvent(self, px, py):
        if px >= self.pos.x and px <= self.pos.x+self.dim.x and py >= self.pos.y and py <= self.pos.y+self.dim.y:
            return self.actionCode
