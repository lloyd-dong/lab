//
//  main.cpp
//  bitmode
//
//  Created by Bo Dong on 1/21/18.
//  Copyright © 2018 Bo Dong. All rights reserved.
//

#include <iostream>

uint64_t data[10];

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}

void pack(uint64_t v, uint32_t bit_count) {
    //assert(bit_mode());
    
    //make_room(bit_count);
    v <<= (64 - bit_count);
    size_t i;
    for (i = 0; i < bit_count; ++i) {
        uint8_t dstByte = m_bits->data[m_bits->off / 8];
        size_t dstBitPos = 7 - (m_bits->off % 8);
        size_t srcBitPos = 63 - i;
        uint8_t m = (uint8_t)(1 & (v >> srcBitPos));
        dstByte |= (m << dstBitPos);
        m_bits->data[m_bits->off / 8] = dstByte;
        m_bits->off++;
    }
}
