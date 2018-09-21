/*
 * library for work with UART
 *
 * autor: wykys
 * verze: 1.0
 * datum: 2.11.2017
 */

#ifndef WYK_UART_H_INCLUDED
#define WYK_UART_H_INCLUDED

#include "settings.h"
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdarg.h>

// ========================================================
void uart_init(void);
void uart_putc(unsigned char data);
void uart_puts(char str[]);
// ========================================================

#endif // WYK_UART_H_INCLUDED
