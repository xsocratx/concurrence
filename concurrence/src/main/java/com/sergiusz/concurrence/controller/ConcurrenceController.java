package com.sergiusz.concurrence.controller;

import com.sergiusz.concurrence.service.ConcurrenceService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/")
public class ConcurrenceController {

    @GetMapping("/primes")
    @ResponseBody
    public Integer getValues(@RequestParam Integer start, @RequestParam Integer end){

        ConcurrenceService concurrenceService = new ConcurrenceService();

        return concurrenceService.getPrimeNumbers(start, end);
    }

}
