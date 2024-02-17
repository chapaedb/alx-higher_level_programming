class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      let rect = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          rect += 'X';
        }
        console.log(rect);
        rect = '';
      }
    } else {
      console.log('Invalid rectangle dimensions.');
    }
  }
};
