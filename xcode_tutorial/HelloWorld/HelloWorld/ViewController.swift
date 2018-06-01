//
//  ViewController.swift
//  HelloWorld
//
//  Created by Bo Dong on 13/03/2017.
//  Copyright © 2017 Bo Dong. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var sayHelloLabel: UILabel!
    let myMessage = "Hello world, hope you are having a good day!"
    
    @IBAction func showPopup(_ sender: Any) {
        
        let alert = UIAlertController(title: "Hello World Message", message: myMessage, preferredStyle: UIAlertControllerStyle.alert)
        //let cancelAction = ULAlertAction
    }

    @IBAction func sayHello(_ sender: Any) {
        var strMessage = "Hello World!"
        sayHelloLabel.text = strMessage
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

