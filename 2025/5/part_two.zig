// 330230312478170 -> too low
//
// 337793378646136 -> too low
// 345095212544114 -> too high

const std = @import("std");

const Range = struct { start: u64, end: u64 };

fn split_id_range(id_range: []const u8) !Range {
    var range_iter = std.mem.splitAny(u8, id_range, "-");
    const start_str = range_iter.first();
    const end_str = range_iter.rest();
    const start = try std.fmt.parseInt(u64, start_str, 10);
    const end = try std.fmt.parseInt(u64, end_str, 10);

    const range: Range = .{
        .start = start,
        .end = end,
    };
    return range;
}

fn check_unique(fresh_id_ranges: std.array_list.Aligned(Range, null), id_range: Range, i: usize, allocator: std.mem.Allocator) !std.array_list.Aligned(Range, null) {
    var valid_ranges: std.ArrayList(Range) = .empty;

    const base_start = id_range.start;
    const base_end = id_range.end;
    const effective_range = fresh_id_ranges.items[i + 1 ..];
    var invalid: usize = 0;
    for (effective_range) |range| {
        const start = range.start;
        const end = range.end;

        const entirely_within: bool = (base_start >= start and base_start <= end) and (base_end >= start and base_end <= end);
        const start_within: bool = (base_start >= start and base_start <= end) and base_end > end;
        const end_within: bool = base_start < start and (base_end >= start and base_end <= end);
        const encompasses: bool = base_start < start and base_end > end;

        if (entirely_within) {
            std.debug.print("Entirely within: {any} vs. {any}\n", .{ id_range, range });
            invalid += 1;
        } else if (start_within) {
            std.debug.print("Start within: {any} vs. {any}\n", .{ id_range, range });
            invalid += 1;

            const new_range: Range = .{
                .start = end + 1,
                .end = base_end,
            };
            const new_valid_ranges = try check_unique(fresh_id_ranges, new_range, i, allocator);
            return new_valid_ranges;
        } else if (end_within) {
            std.debug.print("End within: {any} vs. {any}\n", .{ id_range, range });
            invalid += 1;

            const new_range: Range = .{
                .start = base_start,
                .end = start - 1,
            };
            const new_valid_ranges = try check_unique(fresh_id_ranges, new_range, i, allocator);
            return new_valid_ranges;
        } else if (encompasses) {
            std.debug.print("Encompasses: {any} vs. {any}\n", .{ id_range, range });
            invalid += 1;

            const new_range_a: Range = .{
                .start = base_start,
                .end = start - 1,
            };
            const new_range_b: Range = .{
                .start = end + 1,
                .end = base_end,
            };
            var new_valid_ranges_a = try check_unique(fresh_id_ranges, new_range_a, i + 1, allocator);
            var new_valid_ranges_b = try check_unique(fresh_id_ranges, new_range_b, i + 1, allocator);
            const a_valid: bool = new_valid_ranges_a.items[0].start == new_range_a.start and new_valid_ranges_a.items[0].end == new_range_a.end;
            const b_valid: bool = new_valid_ranges_b.items[0].start == new_range_b.start and new_valid_ranges_b.items[0].end == new_range_b.end;
            if (a_valid and b_valid) {
                std.debug.print("Both valid! {any} vs. {any} -> {any}, {any}\n", .{ id_range, range, new_valid_ranges_a, new_valid_ranges_b });
                std.debug.assert(new_valid_ranges_a.items.len == 1);
                std.debug.assert(new_valid_ranges_b.items.len == 1);
                try new_valid_ranges_a.appendSlice(allocator, new_valid_ranges_b.items);
                defer new_valid_ranges_b.deinit(allocator);
                return new_valid_ranges_a;
            } else if (a_valid) {
                std.debug.print("A valid! {any} vs. {any} -> {any}\n", .{ id_range, range, new_valid_ranges_a });
                defer new_valid_ranges_b.deinit(allocator);
                std.debug.assert(new_valid_ranges_a.items.len == 1);
                return new_valid_ranges_a;
            } else if (b_valid) {
                std.debug.print("B valid! {any} vs. {any} -> {any}\n", .{ id_range, range, new_valid_ranges_b });
                defer new_valid_ranges_a.deinit(allocator);
                std.debug.assert(new_valid_ranges_b.items.len == 1);
                return new_valid_ranges_b;
            } else {
                std.debug.print("None valid! {any} vs. {any}\n", .{ id_range, range });
                defer new_valid_ranges_a.deinit(allocator);
                defer new_valid_ranges_b.deinit(allocator);
            }
        }
    }

    if (invalid == 0) {
        try valid_ranges.append(allocator, id_range);
        std.debug.assert(valid_ranges.items.len == 1);
        return valid_ranges;
    } else {
        const default: Range = .{
            .start = 0,
            .end = 0,
        };
        try valid_ranges.append(allocator, default);
        std.debug.assert(valid_ranges.items.len == 1);
        return valid_ranges;
    }
}

pub fn main() !void {
    const file = try std.fs.cwd().openFile("5/input.txt", .{ .mode = .read_only });
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const file_size: u64 = (try file.stat()).size;
    const buffer: []u8 = try allocator.alloc(u8, file_size);
    defer allocator.free(buffer);

    _ = try file.read(buffer);

    var iter = std.mem.splitAny(u8, buffer, "\n");

    var fresh_id_ranges: std.ArrayList(Range) = .empty;
    defer fresh_id_ranges.deinit(allocator);

    var id_range: bool = true;
    var total_fresh_ids: usize = 0;
    while (iter.next()) |id_or_id_range| {
        const empty_line: bool = std.mem.eql(u8, id_or_id_range, "");
        if (empty_line) {
            id_range = false;
        } else {
            if (id_range & !empty_line) {
                const range = try split_id_range(id_or_id_range);
                try fresh_id_ranges.append(allocator, range);
            }
        }
    }

    var final_id_ranges: std.ArrayList(Range) = .empty;
    defer final_id_ranges.deinit(allocator);
    for (fresh_id_ranges.items, 0..) |fresh_id_range, i| {
        var valid_ranges = try check_unique(fresh_id_ranges, fresh_id_range, i, allocator);
        defer valid_ranges.deinit(allocator);
        std.debug.assert(valid_ranges.items.len <= 2);
        for (valid_ranges.items) |valid_range| {
            if (valid_range.start == 0 and valid_range.end == 0) {
                continue;
            }
            std.debug.print("Valid Range: {any}\n", .{valid_range});
            const fresh_ids = (valid_range.end - valid_range.start) + 1;
            total_fresh_ids += fresh_ids;
            try final_id_ranges.append(allocator, valid_range);
        }
    }

    std.debug.print("Initial size: {d}\n", .{fresh_id_ranges.items.len});
    std.debug.print("Final size: {d}\n", .{final_id_ranges.items.len});

    std.debug.print("{any}\n", .{final_id_ranges});
    std.debug.print("{d}\n", .{total_fresh_ids});
}
