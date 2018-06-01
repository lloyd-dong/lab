//
//  main.m
//  TimeAfterTime
//
//  Created by Bo Dong on 09/08/2017.
//  Copyright © 2017 Bo Dong. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSDate * now = [NSDate date];
        NSLog(@"This NSData object lives at %p ", now);
        // insert code here...
        NSLog(@"The data is %@", now);
    }
    return 0;
}
