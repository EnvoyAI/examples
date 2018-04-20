# EnvoyAI Frequently Asked Questions

## Dev Portal

#### How do I log into the developer portal?
[portal.envoyai.com](https://portal.envoyai.com)

#### How do I learn how to create a machine?
The best way to learn about how to create a machine on the EnvoyAI Platform is to read the [helloworld walk-through](./test-hello/README.md).

#### How do I create a machine that takes a Dicom file as input?
To learn more about DICOM input and other advanced input and output types, please see [TYPES.md](TYPES.md).
To see a simple example that takes a dicom study, series or image as input and returns a dicom study, series or image as output,
see the [test/dicom-study](./test-dicom-study), [test/dicom-series](./test-dicom-series), or [test/dicom-image](./test-dicom-image) example.

#### How do I provide test or sample data for my machine?
For users within your organization you can upload sample data to the "Files"
tab the dev portal. These files will be available to everyone within your
dev portal account's group.

For external users wishing to test your algorithm, we recommend using Google
Drive, or Amazon S3 to publicly host sample images and data. You can then
provide a link to that data in your Dockerfile using the `com.envoyai.info`
LABEL; That link along with all the other information specified will be
shown to all users when they first click on your Machine.

## Security

#### How does Envoy AI protect my docker image?
We recognize the importance of protecting the IP in your docker images. We follow the principle of least privilege in securing docker images. We apply patches, and use 2FA for all EnvoyAI principals. Your docker image is stored within Amazon ECR, that only your organization may access through its own personal IAM policy. We have and will continue to consult with outside security experts. 

#### How is my docker image stored?
We store docker images in Amazon’s Elastic Container Registry (ECR). We administer security on a per-image basis using IAM credentials.

#### Who has access to my image?
Machines in the developer portal are considered private by default. People will only be aware of or have access to your machines if you have granted them that permission explicitly, otherwise, only your organization will have access.

#### How do you manage on-site installations?
If you sell your algorithm to a hospital with an on-site deployment, your docker image will run in the hospital’s data center.
Access to our machines in the data center is limited to a small number of EnvoyAI staff and limited Hospital IT Administrators.
The servers that store and run your docker images have restricted access and a minimal set of open ports. 
The images themselves are run in a very restricted security context to defend against cross-machine attacks.
While hospital staff may theoretically have access to our Dockerhost and thus your docker image, they are contractually
obligated not to try to access or attempt to reverse engineer your IP; doing so would be a crime and would open them to unlimited
liability to damages claimed by you.

## Docker and Machine API

#### How do I quickly adapt an already working dockerfile?
See our [test-echo](./test-echo/Dockerfile) machine for a simple example, or the [caffe-cpp_classification](./caffe-cpp_classification/Dockerfile) machine, an adaption of a caffe image recognition sample, for a slightly more complicated example.

For these examples, we just needed to specify an __ENTRYPOINT__ that would provide the path for the image input, and write the metadata __LABELs__.
The only other required work is to modify the existing project to write the appropriate output files.
See the [Diff](https://github.com/jaketaylorpro/caffe/commit/a90ddca0e384c04d4d0ec0c49e0e7b07c6f0cb07) in our fork of the Caffe repo.

#### How do I view debugging information about my machine when its running on the platform?
All logs, captured from your executable's stdout and stderr, are viewable in the Machine Administration panel, under the logs tab.
We are currently working on expanding debugging and error handling capabilities.

#### How do I get started with Docker?
To download and install Docker please visit [www.docker.com](https://www.docker.com/get-docker)

To learn more about Docker we recommend reading the [docs](https://docs.docker.com/) or viewing 
[this great pluralsight video](https://www.pluralsight.com/courses/docker-deep-dive).

#### Does EnvoyAI Support CUDA?
The EnvoyAI Platform supports nVidia CUDA 9 and CuDNN 6. If your algorithm require a different version, please contact us and we will try to make it available.

Use the __LABEL__ `com.envoyai.nvidia` to enable CUDA support.
```Dockerfile
LABEL com.envoyai.nvidia=true
```

You will likely want to base your Docker image off of an nVidia example.
```Dockerfile
FROM nvidia/cuda:9.0-runtime-ubuntu16.04
```

#### Does EnvoyAI Support OpenCL?
Not quite yet, please contact us if this is a strict requirement for your Machine, and we may be able to prioritize this feature.

#### YAML or JSON
Each of the metadata fields (`com.envoyai.schema-in`,`com.envoyai.schema-out`,`com.envoyai.display`,`com.envoyai.selector`,`com.envoyai.info`)
can be specified with JSON, or with YAML (a superset of JSON that allows us to drop a lot of the cumbersome symbols).
An important "gotcha" when using YAML in a Dockerfile LABEL is that, because the way Docker captures strings, each LABEL must have explicit newline characters using `\n` at the end of each line, and usually a continuation slash so you will see `\n\` at the end of most lines.
See test/echo's [Dockerfile](./test-echo/Dockerfile) for an example that actually mixes yaml and json for brevity and clarity.

#### Can my Machine access the Internet?
Yes and no. Yes for testing and demonstration purposes - we have a configuration
flag that will allow your docker container to access the internet, for example
to make an API call in your own cloud. However installing your algorithm
in most hospitals may not be possible with internet enabled; This may significantly
limit your ability to deploy in for clinical use.

Use the __LABEL__ `com.envoyai.network` to enable network access.
```Dockerfile
LABEL com.envoyai.network=true
```

*Note: if you don't allow network access (the default), the docker container
will not have a /etc/hosts file, and thus requests to localhost will not
 work*
#### Why can't I see GSPS Annotations
Our testing viewer does not currently support GSPS. We hope to provide this feature soon. In the meantime you can use
the free desktop viewer, [Weasis](https://sourceforge.net/projects/dcm4che/files/Weasis/). After importing your study,
make sure to click the green checkbox on the right side of the screen to toggle the annotations on.

#### How should StudyInstanceUID SeriesInstanceUID and SOPInstanceUID be treated?
When creating a secondary capture, structured report, gsps annotations, dicom-rt segmentations,
or dicom-seg segmentations, the newly created dicom instances should all have the same StudyInstanceUID as the original input study
that the instances are derived from, and the new instances should have the same new SeriesInstanceUID and each SOPInstanceUID
should have a new unique SOPInstanceUID.

## Production Clinical Workflow

#### How do I make my Machine ready for a hospital to use it?
There should little to no development needed to make your Machine ready for a hospital. There may be additional standards that you can adopt, or features you can add to make your product more compelling, but in general, if it works on the dev portal, it can be used clinically. See the "Liaison Integration" section of this [related faq](#how-can-my-machine-be-used-and-how-will-it-fit-into-a-hospital-workflow) for more detail.

When you are finished developing a specific version of your Machine and you are ready to distribute it, please contact us and we will create a 'locked down' Read Only repository for that version, so that it can be used with the guarantee that the code will not be changed. This will be the version we deliver for you to hospitals, and this will be the version we demonstrate on our forthcoming physician portal.

#### How can my Machine be used, and how will it fit into a hospital workflow?
There are a number of ways a Machine can be initiated:

1.
    Developer Portal - The Developer portal can be used to test and share
    any Machine with any inputs or outputs.
1.
    _Liaison_ Integration - EnvoyAI's integration edge appliance, which
    lives in hospital data centers, can be configured to receive imaging
    studies from other DICOM endpoints, such as scanners or PACS. _Liaison_
    can be configured to stand up multiple AE Titles which in turn can be
    configured to run any number of Machines with studies send to that AE.
    Once results are computed, they can be delivered to a radiologist in
    a number of ways; for more information see the [related faq](#what-are-the-different-ways-my-machines-results-can-be-used)
    or [envoyai.com](http://envoyai.com).

    Currently liaison can only run machines that take a single
    DICOM study, along with configuration inputs (that may be hardcoded).
    Future development will allow multiple DICOM study inputs (ie priors
    or comparisons), and other data inputs from HL7 sources.
1.
    Other Integration - EnvoyAI is continually working on additional
    distribution partnerships. One example of such a partnership is that
    with [AmbraHealth](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0ahUKEwiD1saewbvaAhWGjlkKHSNJDjoQFgg8MAI&url=https%3A%2F%2Fwww.auntminnie.com%2Findex.aspx%3Fsec%3Dlog%26itemID%3D120142&usg=AOvVaw1Op0I0PRlwuWW1gLySOcV5).
    Integration details in these cases will vary.

#### What are the different ways my Machine's results can be used?
There are a few ways Machine's results can be viewed or otherwise used,
EnvoyAI is continually working on additional features and integration
partnerships, so these capabilities will expand over time.

1.
    On the dev portal - Results can be seen by anyone, via a web browser,
    that you grant access; all data types are supported.

1.
    On the forthcoming Physician portal - Results for *live* versions of
    Machines (Machine version no longer in development) will be viewable
    by Physicians in an easy to use interface. The Physician portal will
    allow potential users to test and demonstrate Machine's before
    purchasing and integrating at their hospital.

1.
    In a hospital, the ways that results can be used will vary based on
    the availability of other systems, and the configurability of said
    systems. Liaison's open REST API makes the integration options almost
    limitless. That aside, here are the common configuration we currently
    can implement, along with some configurations that we are in the
    process of developing.

    1.
        DICOM integration - _Liaison_ can be configured to send DICOM
        results to one or more DICOM endpoint, usually PACS. This means DICOM
        GSPS (Annotation), SR (Structured Report), SC (Secondary Capture)
        results will all be sent to PACS and viewed either with the bundled
        PACS viewer or with an advanced viewer contextually launched from the PACS.

        With this integration, non-DICOM types cannot be sent to PACS, and will be ignored.

    1.
        Viewer integration - _Liaison_ provides REST API routes
        designed to provide viewers Machine results. The full
        features of the viewer will vary product to product. Currently
        the only fully integrated viewer is TeraRecon's forthcoming, *NorthStar*.
        We hope to add other deeply integrated viewers in the future.

        Viewer's have the capability to display more than just DICOM outputs,
        NorthStar for example can display JPG, PNGs, PDFs, as well as text and
        measurement data from JSON.

        An example of the more advanced behaviors that an integrated viewer can enable
        is NorthStar's ability to let the user *Accept* or *Reject* results
        before they are archived to PACS, so that only correct results get saved.

    1.
        *PENDING* Reporting integration - _Liaison_ provides REST API routes
        designed to provide radiology reporting systems with Machine results.
        This will allow measurements to reach EMRs without needing to be
        dictated or copied, or perhaps double check physicians if they are
        missing a critical finding.

    1.
        *PENDING* Worklist and Notification System integration - _Liaison_
        provides results via REST API routes that Worklist and Notification Systems
        can leverage to order a physician's work, or to send notifications
        when there are critical findings.

