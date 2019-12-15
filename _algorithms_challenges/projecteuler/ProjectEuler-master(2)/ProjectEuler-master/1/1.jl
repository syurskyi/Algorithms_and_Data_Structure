function sum_of_multiple(multiple, bound)
    multiple_bound = bound - (bound % multiple)
    return multiple_bound * (multiple_bound // multiple + 1) // 2
end

function get(bound)
    included = bound - 1
    return sum_of_multiple(3, included) + sum_of_multiple(5, included) - sum_of_multiple(15, included)
end

function main()
    println(get(10))
    println(get(1000))
end

main()
