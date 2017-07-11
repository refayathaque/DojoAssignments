package com.refayathaque.pets.models;

public class Dog extends Animal {
	public Dog() {}
	
	public Dog(String name, String breed, double weight) {
		this.setName(name);
		this.setBreed(breed);
		this.setWeight(weight);
	}
	
	@Override
	public String showAffection() {
		if(this.getWeight() >= 30.0) {
			return this.getName() + " curled up next to you.";
		}
		else if(this.getWeight() < 30.0) {
			return this.getName() + " hopped in your lap.";
		}
		else {
			return "";
		}
	}
	
	
}
