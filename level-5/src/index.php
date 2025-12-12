<?php
/**
 * Contacts Manager
 * A simple contact management system with sortable columns
 */

// Sample contacts data
$contacts = [
    [
        'name' => 'Sarah Johnson',
        'email' => 'sarah.johnson@techcorp.com',
        'company' => 'TechCorp Industries',
        'position' => 'Senior Developer',
        'phone' => '+1-555-0123'
    ],
    [
        'name' => 'Michael Chen',
        'email' => 'mchen@innovate.io',
        'company' => 'Innovate Solutions',
        'position' => 'Project Manager',
        'phone' => '+1-555-0456'
    ],
    [
        'name' => 'Emily Rodriguez',
        'email' => 'emily.r@dataflow.com',
        'company' => 'DataFlow Systems',
        'position' => 'Data Analyst',
        'phone' => '+1-555-0789'
    ],
    [
        'name' => 'James Wilson',
        'email' => 'jwilson@cloudnet.com',
        'company' => 'CloudNet Services',
        'position' => 'DevOps Engineer',
        'phone' => '+1-555-0321'
    ],
    [
        'name' => 'Amanda Foster',
        'email' => 'afoster@nexustech.com',
        'company' => 'Nexus Technologies',
        'position' => 'UX Designer',
        'phone' => '+1-555-0654'
    ],
    [
        'name' => 'David Kim',
        'email' => 'david.kim@alphasoft.com',
        'company' => 'AlphaSoft Inc',
        'position' => 'Software Architect',
        'phone' => '+1-555-0987'
    ],
    [
        'name' => 'Lisa Martinez',
        'email' => 'lmartinez@betaworks.com',
        'company' => 'BetaWorks LLC',
        'position' => 'Product Owner',
        'phone' => '+1-555-0147'
    ],
    [
        'name' => 'Robert Taylor',
        'email' => 'rtaylor@gammadev.com',
        'company' => 'Gamma Development',
        'position' => 'Lead Engineer',
        'phone' => '+1-555-0258'
    ],
    [
        'name' => 'Jennifer Lee',
        'email' => 'jlee@deltatech.com',
        'company' => 'Delta Technologies',
        'position' => 'QA Specialist',
        'phone' => '+1-555-0369'
    ],
    [
        'name' => 'Christopher Brown',
        'email' => 'cbrown@epsilonsys.com',
        'company' => 'Epsilon Systems',
        'position' => 'Security Engineer',
        'phone' => '+1-555-0741'
    ]
];

// Get sort parameter from query string
$sortBy = isset($_GET['sort']) ? $_GET['sort'] : 'name';

// Map of allowed sort fields to their comparison functions
$sortFunctions = [
    'name' => 'compareByName',
    'email' => 'compareByEmail',
    'company' => 'compareByCompany',
    'position' => 'compareByPosition',
    'phone' => 'compareByPhone'
];

// Define comparison functions for each field
function compareByName($a, $b) {
    return strcasecmp($a['name'], $b['name']);
}

function compareByEmail($a, $b) {
    return strcasecmp($a['email'], $b['email']);
}

function compareByCompany($a, $b) {
    return strcasecmp($a['company'], $b['company']);
}

function compareByPosition($a, $b) {
    return strcasecmp($a['position'], $b['position']);
}

function compareByPhone($a, $b) {
    return strcasecmp($a['phone'], $b['phone']);
}

// Get the callback function name
// Use the mapped function if available, otherwise use the raw input
$callback = isset($sortFunctions[$sortBy]) ? $sortFunctions[$sortBy] : $sortBy;

// Sort contacts using the callback
usort($contacts, $callback);


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacts Manager</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>📇 Contacts Manager</h1>
            <p class="subtitle">Manage and organize your business contacts</p>
        </header>

        <main>
            <div class="table-wrapper">
                <table class="contacts-table">
                    <thead>
                        <tr>
                            <th><a href="?sort=name">Name</a></th>
                            <th><a href="?sort=email">Email</a></th>
                            <th><a href="?sort=company">Company</a></th>
                            <th><a href="?sort=position">Position</a></th>
                            <th><a href="?sort=phone">Phone</a></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($contacts as $contact): ?>
                        <tr>
                            <td class="name-cell"><?php echo htmlspecialchars($contact['name']); ?></td>
                            <td><?php echo htmlspecialchars($contact['email']); ?></td>
                            <td><?php echo htmlspecialchars($contact['company']); ?></td>
                            <td><?php echo htmlspecialchars($contact['position']); ?></td>
                            <td><?php echo htmlspecialchars($contact['phone']); ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </tbody>
                </table>
            </div>

            <div class="info-box">
                <p><strong>Total Contacts:</strong> <?php echo count($contacts); ?></p>
                <p><strong>Sorted by:</strong> <?php echo htmlspecialchars(ucfirst($sortBy)); ?></p>
            </div>
        </main>

        <footer>
            <p>&copy; 2024 Contacts Manager. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
