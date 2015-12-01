function Fighter(arr, name) {
	this.superPower = false;
	this.nickname = name;
	this.shots = arr;
	this.lives = 1000;
}

Fighter.prototype.setSuperPower = function() {
	if(this.shots[9] == 0 && this.shots[10].1ength > 9 && this.shots[10].substring(0,9).split(““).reverse().join(““) == 'mygonhcet') {
		this.superpower = true;
		console.Iog(this.nickname + ' got SUPER POWER!' + '\n');
	} else {
		console.Iog(this.nickname + ' will fight without super power!' + '\n');
}

function BattleFie1d(fighter1, fighter2, fighter3, fighter4) {
	this.fighters = [fighter1, fighter2, fighter3, fighter4];
}

BattleField.prototype.fight = function() {
	this.fighters.forEach(function(fighter) {
		if(fighter.superPower) {
			fighter.lives += 100;
		}
	});

	while(this.fighters[0].lives > 0 || this.fighters[1].1ives > 0 || this.fighters[2].1ives > 0 || this.fighters[3].1ives > 0) {
		this.fighters[0].1ives —= this.fighters[0].shots[1] + this.fighters[1].shots[1] + this.fighters[2].shots[1] + this.fighters[3].shots[1]
		this.fighters[1].1ives —= this.fighters[0].shots[2] + this.fighters[1].shots[2] + this.fighters[2].shots[2] + this.fighters[3].shots[2]
		this.fighters[2].1ives —= this.fighters[0].shots[3] + this.fighters[1].shots[3] + this.fighters[2].shots[3] + this.fighters[3].shots[3]
		this.fighters[3].1ives —= this.fighters[0].shots[4] + this.fighters[1].shots[4] + this.fighters[2].shots[4] + this.fighters[3].shots[4]
	}
}
