package com.company

/**
  * Created by bodong on 01/05/2017.
  */
object Hello {

  def test():Unit ={
    val a= Array(1,2,3)
    val b=Array(4,5,6)

    //a.zip(b).map( (x:Int,y:Int) => {x+y})

    println("\n------")
    for (x <- a zip b){
      print(x)
    }

  }
  def main(args: Array[String]):Unit ={
    print("hello")
    test
  }

}
