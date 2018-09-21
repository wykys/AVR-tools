#include "uart.h"

void uart_init(void)
{
    unsigned int ubrr = F_CPU / 16 / 9600 - 1;
    UBRR0   = ubrr;                        // 9600 bps
    UCSR0B  = (1 << RXEN0) | (1 << TXEN0); // enable receiver and transmitter
    UCSR0C  = 3 << UCSZ00;                 // 8n1
    UCSR0B |= 1 << RXCIE0;                 // receiver interrupt
    sei();
}

void uart_putc(unsigned char data)
{
    /* Wait for empty transmit buffer */
    while (!( UCSR0A & (1 << UDRE0)) )
        ;
    /* Put data into buffer, sends the data */
    UDR0 = data;
}

void uart_puts(char str[])
{
    for (int i = 0; str[i]; i++)
        uart_putc(str[i]);
}
